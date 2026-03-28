import json
import os
import subprocess
import sys
import tempfile

import nbformat
from nbformat.v4 import new_code_cell, new_notebook

from src.settings import settings

os.environ["KAGGLE_API_TOKEN"] = settings.kaggle_api_token

METADATA = {
    "id": f"{settings.kaggle_username}/{settings.kaggle_sub_kernel_slug}",
    "title": settings.kaggle_sub_kernel_slug,
    "code_file": "sub.ipynb",
    "language": "python",
    "kernel_type": "notebook",
    "is_private": "true",
    "enable_gpu": "true",
    "enable_tpu": "false",
    "enable_internet": "false",
    "dataset_sources": [f"{settings.kaggle_username}/{settings.kaggle_dataset_slug}"],
    "competition_sources": [settings.kaggle_competition_name],
    "kernel_sources": [f"{settings.kaggle_username}/{settings.kaggle_kernel_slug}"],
    "model_sources": [],
}


def main() -> None:
    # 実行する実験番号を取得. 引数で設定されていればそれを使用し、なければ exp/ 内の最大番号を使う
    if len(sys.argv) > 1:
        exp = sys.argv[1]
    else:
        dirs = sorted(d for d in os.listdir("exp") if d.isdigit())
        if not dirs:
            raise FileNotFoundError("exp/ に実験ディレクトリが見つからない")
        exp = dirs[-1]

    install_cell = (
        f"%pip install {settings.kaggle_kernel_slug}/*.whl"
        f" --force-reinstall --root-user-action ignore"
        f" --no-deps --no-index --find-links {settings.kaggle_kernel_slug}"
    )
    run_cell = (
        f"import os\n"
        f'os.environ["PYTHONPATH"] = "{settings.kaggle_dataset_slug}"\n'
        f'!python "{settings.kaggle_dataset_slug}/{exp}/run.py"'
    )

    nb = new_notebook(cells=[new_code_cell(source=install_cell), new_code_cell(source=run_cell)])
    nb["metadata"]["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "sub.ipynb"), "w") as f:
            nbformat.write(nb, f)

        with open(os.path.join(tmpdir, "kernel-metadata.json"), "w") as f:
            json.dump(METADATA, f, indent=2)

        subprocess.run(
            ["kaggle", "kernels", "push", "-p", tmpdir],
            check=True,
        )


if __name__ == "__main__":
    main()

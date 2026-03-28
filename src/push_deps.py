import json
import os
import subprocess
import tempfile
import tomllib

import nbformat
from nbformat.v4 import new_code_cell, new_notebook
from packaging.requirements import Requirement

from src.settings import settings

METADATA_TEMPLATE = {
    "id": f"{settings.KAGGLE_USERNAME}/{settings.KAGGLE_KERNEL_SLUG}",
    "title": settings.KAGGLE_KERNEL_SLUG,
    "code_file": "code.ipynb",
    "language": "python",
    "kernel_type": "notebook",
    "is_private": "true",
    "enable_gpu": "false",
    "enable_tpu": "false",
    "enable_internet": "true",
    "dataset_sources": [],
    "competition_sources": [],
    "kernel_sources": [],
    "model_sources": [],
}


def build_notebook(pkgs: list[str]) -> nbformat.NotebookNode:
    """各パッケージを pip download / install するノートブックを生成する。"""
    download = "!pip download -d /kaggle/working " + " ".join(pkgs)
    install = (
        "!pip install /kaggle/working/*.whl"
        " --force-reinstall --root-user-action ignore"
        " --no-deps --no-index --find-links /kaggle/working"
    )
    nb = new_notebook(cells=[new_code_cell(source=f"{download}\n{install}")])
    nb["metadata"]["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }
    return nb


def main() -> None:
    # pyproject.toml からパッケージ名を抽出
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    deps = pyproject["project"]["dependencies"]
    pkgs = [Requirement(d).name for d in deps]

    with tempfile.TemporaryDirectory() as tmpdir:
        # notebook 作成
        nb = build_notebook(pkgs)
        with open(os.path.join(tmpdir, "code.ipynb"), "w") as f:
            nbformat.write(nb, f)

        # kernel-metadata.json 作成
        with open(os.path.join(tmpdir, "kernel-metadata.json"), "w") as f:
            json.dump(METADATA_TEMPLATE, f, indent=2)

        # 3.Kaggle に push
        os.environ["KAGGLE_API_TOKEN"] = settings.KAGGLE_API_TOKEN
        subprocess.run(
            ["kaggle", "kernels", "push", "-p", tmpdir],
            check=True,
        )


if __name__ == "__main__":
    main()

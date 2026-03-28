import json
import os
import subprocess
from pathlib import Path

from src.settings import settings

os.environ["KAGGLE_API_TOKEN"] = settings.kaggle_api_token

METADATA = {
    "title": settings.kaggle_dataset_slug,
    "id": f"{settings.kaggle_username}/{settings.kaggle_dataset_slug}",
    "licenses": [{"name": "CC0-1.0"}],
}


def main() -> None:
    with open(Path("exp", "dataset-metadata.json"), "w") as f:
        json.dump(METADATA, f, indent=2)

    # datasets version update を試し、失敗したら datasets create
    result = subprocess.run(
        ["kaggle", "datasets", "version", "-p", "exp", "-m", "update codes"],
    )
    if result.returncode != 0:
        subprocess.run(
            ["kaggle", "datasets", "create", "-p", "exp"],
            check=True,
        )


if __name__ == "__main__":
    main()

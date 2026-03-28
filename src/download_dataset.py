import os
import subprocess

from src.settings import settings

os.environ["KAGGLE_API_TOKEN"] = settings.kaggle_api_token


def main() -> None:
    subprocess.run(
        [
            "kaggle",
            "competitions",
            "download",
            "-c",
            settings.kaggle_competition_name,
            "-p",
            "data",
        ],
        check=True,
    )

    # ダウンロードした zip を展開して削除
    zip_path = f"data/{settings.kaggle_competition_name}.zip"
    subprocess.run(
        ["unzip", "-o", zip_path, "-d", "data"],
        check=True,
    )
    os.remove(zip_path)


if __name__ == "__main__":
    main()

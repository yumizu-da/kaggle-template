# kaggle-template

Kaggleコンペティション用のテンプレートリポジトリ

## Environment

Dockerコンテナを起動

```bash
docker compose up -d --build
```

## 初回設定

### 1. 環境変数の設定

```bash
cp .env.sample .env
```

.env ファイルを編集

```bash
KAGGLE_USERNAME=your_username
KAGGLE_API_TOKEN=your_api_token
KAGGLE_COMPETITION_NAME=competition_name
```

- `KAGGLE_API_TOKEN`はKaggleページから、Settings → API → Generate New Tokenで取得可能
- `KAGGLE_COMPETITION_NAME`はURLから取得可能（`https://www.kaggle.com/competitions/{KAGGLE_COMPETITION_NAME}`）

### 2. データセットをローカル環境にダウンロード

```python
uv run src/download_dataset.py
```

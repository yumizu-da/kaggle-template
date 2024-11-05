# kaggle-template

Kaggleコンペティション用のテンプレートリポジトリ

## Environment

Dockerコンテナを起動

```bash
docker compose up -d --build
```

## 初回設定

以下の記事にならってVSCode上で開発を行い、Kaggle CLI 経由でデータをアップロードするようにします。kaggleページ上では基本的にはコードの提出のみを行います。

<https://ho.lc/blog/kaggle_code_submission/>

> [!NOTE]
> 以下の説明で不明点があれば、上記記事を参照してください。全てこちらに書かれています

### 1. kaggleAPIを取得し、`.kaggle/kaggle.json`に記載

[この記事](https://qiita.com/5sigma_AAA/items/791cca3214a89b9d1201)を参考にしました。体裁は`.kaggel/kaggle_sample.json`を参考にしてください

### 2. データセットをローカル環境にダウンロード

kaggleAPI経由で`data`ディレクトリにダウンロードします

```bash
kaggle competitions download -c eedi-mining-misconceptions-in-mathematics -p data && \
unzip data/eedi-mining-misconceptions-in-mathematics.zip -d data && \
rm data/eedi-mining-misconceptions-in-mathematics.zip
```

### 3. 実験コード管理設定（`exp`以下）

実験コードをkaggle Datasetにアップロードするための設定です

1. `exp`内に`dataset-metadata.json`を用意し、適宜書き換え
2. `make init_exp`を実行し、実験コードのkaggle Datasetを作成

### 4. wheelパッケージ管理設定(`deps`以下)

`pip install`したいパッケージを用意するnotebookを用意します \
kaggle code competitionでは、インターネットOFF環境で提出します。そのためpip installする際は、事前にwheelファイルをダウンロードするnotebookを用意しておいて、kaggle上で実行しておく必要があります

1. `deps`ディレクトリに`kernel-metadata.json`を用意し、適宜書き換え
2. `deps.ipynb`に必要なパッケージを追加
3. `make upload_deps`を実行し、notebookを更新

### 5. submission用のコード管理（`sub`以下）

kaggleに予測結果を投稿するためのnotebookを用意します

1. `sub`内に`kernel-metadata.json`を用意し、適宜書き換え
2. `make upload_sub`を実行し、submission用のkaggle Datasetをアップロード

## コード提出手順

更新した`exp`、`deps`以下の内容を全てkaggleにアップロードし、最後に`sub`以下のnotebookを提出します

```bash
make submit
```

## TODO

- [ ] Dockerfileの整理
- [ ] 各jsonファイルを汎用的にする

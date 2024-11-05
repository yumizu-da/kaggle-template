# https://github.com/Kaggle/docker-python/releases
FROM gcr.io/kaggle-gpu-images/python:v150

# NOTE: RTX3060環境では、用意されているPytorchが動かないので再インストール
RUN python3 -m pip install --upgrade pip && \
    pip uninstall torch torchvision -y && \
    pip install --no-cache-dir \
    torch==2.1.2+cu121 -f https://download.pytorch.org/whl/cu121/torch \
    torchvision==0.16.2+cu121 -f https://download.pytorch.org/whl/cu121/torchvision \
    torchaudio==2.1.2+cu121 -f https://download.pytorch.org/whl/cu121/torchaudio

# その他のライブラリ
RUN pip install --no-cache-dir \
    ruff \
    hydra-core

WORKDIR /kaggle/working
ENV KAGGLE_CONFIG_DIR=/kaggle/working/.kaggle

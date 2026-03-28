# https://github.com/Kaggle/docker-python/releases
ARG PLATFORM=linux/amd64
FROM --platform=$PLATFORM gcr.io/kaggle-gpu-images/python:latest

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /kaggle/working
ENV KAGGLE_CONFIG_DIR=/kaggle/working/.kaggle

COPY pyproject.toml uv.lock README.md .
RUN uv sync

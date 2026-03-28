# https://github.com/Kaggle/docker-python/releases
FROM gcr.io/kaggle-gpu-images/python:latest

WORKDIR /kaggle/working
ENV PATH="/root/.local/bin/:${PATH}"

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY .python-version pyproject.toml uv.lock README.md ./
RUN uv python pin "$(cat .python-version)" && \
    uv sync --extra kaggle --dev

CMD ["/bin/bash"]

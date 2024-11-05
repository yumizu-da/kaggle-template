import os
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd  # type: ignore
from hydra import compose, initialize

if "KAGGLE_KERNEL_RUN_TYPE" in os.environ:
    env = "kaggle"
else:
    env = "local"

with initialize(config_path="config", version_base=None):
    cfg = compose(config_name="config", overrides=[f"dir={env}"])
    cfg.exp_number = Path().resolve().name

test_df = pd.read_csv(cfg.dir.test_csv_path)

# 提出物の作成. 適当にランダムな値を入れている
sub_df = pd.DataFrame(
    {
        "id": test_df["id"],
        "target": np.random.rand(len(test_df)),
    }
)
sub_df.to_csv("submission.csv", index=False)

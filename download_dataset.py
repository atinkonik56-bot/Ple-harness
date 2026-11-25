#!/usr/bin/env python3
"""Download the full PLE dataset (google/physical-engineerings-last-exam, ~955 MB)
via huggingface_hub snapshot_download, using the dynamic-credential surrogate.
Resumable: snapshot_download skips files already present.
Log: ~/workspace/kaggle-ple/data/download.log
"""
import os
import sys

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import dynamic_credential_entry

entry = dynamic_credential_entry("custom.huggingface", "access_token")
surrogate = str(entry["surrogate"]).strip()

from huggingface_hub import snapshot_download

out = snapshot_download(
    repo_id="google/physical-engineerings-last-exam",
    repo_type="dataset",
    token=surrogate,
    local_dir=os.path.expanduser("~/workspace/kaggle-ple/data"),
)
print("DOWNLOAD COMPLETE:", out)

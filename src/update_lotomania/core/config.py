import os
from pathlib import Path

__all__ = ['original_file', 'destination_file']

LOTOMANIA_ORIGIN_FILE = os.getenv("LOTOMANIA_ORIGIN_FILE")
LOTOMANIA_DESTINATION_FILE = os.getenv("LOTOMANIA_DESTINATION_FILE")

if not LOTOMANIA_ORIGIN_FILE or not LOTOMANIA_DESTINATION_FILE:
    raise ValueError("LOTOMANIA_ORIGIN_FILE and LOTOMANIA_DESTINATION_FILE are required env variables")

original_file = Path(LOTOMANIA_ORIGIN_FILE)
destination_file = Path(LOTOMANIA_DESTINATION_FILE)

if not original_file.exists():
    raise FileNotFoundError(f"File {original_file} not found")

if not destination_file.parent.exists():
    raise FileExistsError(f"Directory {destination_file.parent} not found")

import os
from pathlib import Path

__all__ = ['API_HOST', 'FILE_DIR', 'LOTOMANIA_ORIGIN_FILE', 'LOTOMANIA_DESTINATION_FILE']

HOME = Path.home()

API_HOST = HOME / 'Projetos' / 'GitHub' / 'API-Lotomania'
FILE_DIR = HOME / 'Downloads' / 'Lotomania'

LOTOMANIA_ORIGIN_FILE = FILE_DIR / 'Lotomania.xlsx'
LOTOMANIA_DESTINATION_FILE = API_HOST / 'core' / 'data' / 'file' / 'lotomania.csv'

if not API_HOST.exists():
    raise FileNotFoundError(f"Directory {API_HOST} not found")

if not FILE_DIR.exists():
    raise FileNotFoundError(f"Directory {FILE_DIR} not found")

if not LOTOMANIA_ORIGIN_FILE.exists():
    raise FileNotFoundError(f"File {LOTOMANIA_ORIGIN_FILE} not found")

if not LOTOMANIA_DESTINATION_FILE.parent.exists():
    raise FileExistsError(f"Directory {LOTOMANIA_DESTINATION_FILE.parent} not found")


import os
from pathlib import Path

__all__ = ['API_HOST', 'FILE_XLSX', 'OUTPUT_FILE_CSV']


local_files = Path(__file__).parent.parent.joinpath('files')

API_HOST = os.getenv('API_LOTOMANIA_HOST')
FILE_XLSX = os.getenv('FILE_LOTOMANIA_XLSX')

if not API_HOST:
    raise ValueError("API_LOTOMANIA_HOST is not defined in the environment variables")

if not FILE_XLSX:
    raise ValueError("FILE_LOTOMANIA_XLSX is not defined in the environment variables")

API_HOST = Path(API_HOST)
FILE_XLSX = Path(FILE_XLSX)

if not API_HOST.exists():
    raise FileNotFoundError(f"Directory {API_HOST} not found")

if not FILE_XLSX.exists():
    raise FileNotFoundError(f"File {FILE_XLSX} not found")

OUTPUT_FILE_CSV = API_HOST / 'core' / 'data' / 'file' / 'lotomania.csv'

if not OUTPUT_FILE_CSV.parent.exists():
    raise FileExistsError(f"Directory {OUTPUT_FILE_CSV.parent} not found")

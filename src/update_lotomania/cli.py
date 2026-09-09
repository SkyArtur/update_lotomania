from csv_converter import csv_converter
from .core import FILE_XLSX, OUTPUT_FILE_CSV, handler_atualizar_sorteios

def main() -> None:
    csv_converter(FILE_XLSX, OUTPUT_FILE_CSV)
    handler_atualizar_sorteios()


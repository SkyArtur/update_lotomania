from csv_converter import csv_converter
from .core import LOTOMANIA_ORIGIN_FILE, LOTOMANIA_DESTINATION_FILE, update_api

def main() -> None:
    csv_converter(LOTOMANIA_ORIGIN_FILE, LOTOMANIA_DESTINATION_FILE)
    update_api()


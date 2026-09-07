def main() -> None:
    from csv_converter import csv_converter
    from .core.config import original_file, destination_file
    csv_converter(original_file, destination_file)


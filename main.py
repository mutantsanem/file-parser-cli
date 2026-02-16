import sys
import os

from parsers.txt_parser import parse_txt
from parsers.csv_parser import parse_csv
from parsers.json_parser import parse_json


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        return

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("File does not exist")
        return

    extension = file_path.split(".")[-1].lower()

    if extension == "txt":
        result = parse_txt(file_path)
    elif extension == "csv":
        result = parse_csv(file_path)
    elif extension == "json":
        result = parse_json(file_path)
    else:
        print("Unsupported file type")
        return

    print("\n--- File Summary ---")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

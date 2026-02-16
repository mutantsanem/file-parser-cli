import csv

def parse_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))

    return {
        "type": "CSV",
        "rows": len(reader),
        "columns": len(reader[0]) if reader else 0
    }

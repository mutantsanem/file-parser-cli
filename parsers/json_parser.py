import json

// JSON parser function
def parse_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return {
        "type": "JSON",
        "keys": len(data) if isinstance(data, dict) else "Not a dict"
    }

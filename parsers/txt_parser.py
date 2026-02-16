def parse_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    words = content.split()

    return {
        "type": "TXT",
        "lines": len(lines),
        "words": len(words),
        "characters": len(content)
    }

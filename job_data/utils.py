import json


def read_json(path: str) -> dict:
    with open(file=path, mode='r', encoding='utf-8') as f:
        return json.load(f)
    
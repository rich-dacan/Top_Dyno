
import json


def read_json(filepath: str) -> list[dict]:
    with open(filepath, 'r') as file:
        return json.load(file)


def write_json(filepath: str, data: list[dict]) -> None:
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2, ascii=False)

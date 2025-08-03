import os
import yaml
import json
from typing import Dict, Any

def read_yaml_file(file_path:str) -> Any | None:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Yaml file not found at path: {file_path}")
    with open(file_path, "r") as file:
        yaml_content: Any | None = yaml.safe_load(file)
        return yaml_content


def read_json_file(file_path: str) -> Any:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JSON file not found at path: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            json_content: Any = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file '{file_path}': {e}") from e
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while reading '{file_path}': {e}") from e
    return json_content
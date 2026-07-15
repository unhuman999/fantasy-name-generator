import json
from src.models import RacesDataset

def load_dataset(file_path: str)-> dict:
    with open(file_path, 'r', encoding="utf-8") as file:
        raw_data = json.load(file)
    validate= RacesDataset.model_validate(raw_data)
    validated_data=validate.model_dump()
    return validated_data



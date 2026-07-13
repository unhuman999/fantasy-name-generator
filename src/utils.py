import json
from src.models import RacesDataset
from pydantic import ValidationError

def load_dataset(file_path: str)-> dict:
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            raw_data = json.load(file)
        validate= RacesDataset.model_validate(raw_data)
        validated_data=validate.model_dump()
        return validated_data

    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {file_path} поврежден")
        return{}
    
    except (ValidationError, TypeError, ValueError):
        print("Ошибка! Битая строка!")
        return{}
        

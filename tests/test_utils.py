import json
from src.utils import load_dataset
import pytest
from pydantic import ValidationError


def test_load_dataset_file_not_found(tmp_path):
    missing_file = tmp_path / "nonexistent.json"
    with pytest.raises(FileNotFoundError):
        load_dataset(str(missing_file))

def test_load_dataset_invalid_json(tmp_path):
    corrupted_file = tmp_path / "damaged.json"
    corrupted_file.write_text("{", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        load_dataset(str(corrupted_file))

def test_load_dataset_non_conforming_structure(tmp_path):
    invalid_data = {"elf":{"male":"Legolas", "female":["Arwen"]}}
    invalid_file = tmp_path / "valuenotlist.json"
    invalid_file.write_text(json.dumps(invalid_data), encoding="utf-8")
    with pytest.raises(ValidationError):
        load_dataset(str(invalid_file))

def test_load_correct(tmp_path):
    valid_data = {"elf": {"male": ["Legolas"],"female": ["Arwen"]}}
    valid_file = tmp_path / "validdataset.json"
    valid_file.write_text(json.dumps(valid_data), encoding="utf-8")
    result =  load_dataset(str(valid_file))
    assert result == valid_data 
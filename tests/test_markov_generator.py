import pytest
import random
from src.markov_generator import capitalize_name, build_markov_model, serialize_model, deserialize_model, save_model, load_model, markov_generate, END_TOKEN


def test_capitalize_name_simple_name():
    assert capitalize_name("brian") == "Brian"

def test_capitalize_name_after_apostrophe():
    assert capitalize_name("o'connor") == "O'Connor"

def test_capitalize_name_after_hyphen():
    assert capitalize_name("iron-fist") == "Iron-Fist"

def test_capitalize_name_apostrophe_at_end():
    assert capitalize_name("test'") == "Test'"

def test_capitalize_name_hyphen_at_end():
    assert capitalize_name("test-") == "Test-"

def test_capitalize_name_empty_name():
    assert capitalize_name("") == ""



def test_build_markov_model_empty_list():
    with pytest.raises(ValueError): build_markov_model([])

def test_build_markov_model_names_shorter_than_order():
    names = ["a", "ab", "xy"]
    with pytest.raises(ValueError): build_markov_model(names)

def test_build_markov_model_single_name_structure():
    model = build_markov_model(["name"])
    assert model["avg_length"] == 4
    assert model["starts"] == {"nam": 1}
    assert model["transitions"]["nam"] == {"e": 1}
    assert model["transitions"]["ame"] == {END_TOKEN: 1}


def test_serialize_deserialize_model_round_trip():
    model = build_markov_model(["name", "surname"])
    serialized = serialize_model(model)
    restored = deserialize_model(serialized)
    assert restored == model

def test_save_load_model_round_trip(tmp_path):
    model = build_markov_model(["male", "surname"])
    path = tmp_path / "test_model.json"
    save_model(model, path)
    loaded_model = load_model(path)
    assert loaded_model == model


def test_markov_generate_seed_result():
    model = build_markov_model(["male", "female"])
    rng = random.Random(67)
    result = markov_generate(model, rng)
    assert result == "Male"
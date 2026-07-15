from src.generator import generate_hybrid_name, generate_name, random_names
import pytest 
import random

def test_generate_hybrid_name_basic():
    result = generate_hybrid_name("Addemios", "Adorellan")
    assert result == "Addeellan"

def test_generate_hybrid_name_single_char_name():
    result = generate_hybrid_name("A", "Balin")
    assert result == "Lin"

def test_generate_hybrid_name_odd_length():
    result = generate_hybrid_name("Elric", "Brom")
    assert result == "Elom"

def test_generate_hybrid_name_empty_first_name():
    result = generate_hybrid_name("", "Balin")
    assert result == "Lin"

def test_generate_hybrid_name_empty_second_name():
    result = generate_hybrid_name("Thorin", "")
    assert result == "Tho"

@pytest.mark.xfail(reason="capitalize() converts letters following the apostrophe to lowercase")
def test_generate_hybrid_name_preserves_internal_capital():
    result = generate_hybrid_name("Thorin", "Ka'Rhen")
    assert result == "ThoRhen"

def test_generate_name_seed_detected():
    races_data = {
        "elf": {
            "male": ["Legolas", "Elrond", "Thranduil"],
            "female": ["Arwen"]
        }
    }
    rng = random.Random(67)
    result = generate_name("elf", "male", races_data, rng)
    assert result == "Legolas"

def test_generate_name_empty_list():
    races_data = {
        "elf": {
            "male": [],
            "female": ["Arwen"]
        }
    }
    with pytest.raises(ValueError):
        generate_name("elf", "male", races_data)

def test_random_names_seed_detected():
    races_data = {
        "elf": {
            "male": ["Legolas", "Elrond", "Thranduil"],
            "female": ["Arwen", "Abyssal", "Adras"]
        }
    }

    rng = random.Random(67)

    result = random_names("elf", "male", races_data, rng)
    assert result == ('Legolas', 'Thranduil')

def test_random_names_short_list():
    races_data = {
        "elf": {
            "male": ["Legolas"],
            "female": ["Arwen", "Abyssal", "Adras"]
        }
    }
    with pytest.raises(ValueError):
        random_names("elf", "male", races_data)
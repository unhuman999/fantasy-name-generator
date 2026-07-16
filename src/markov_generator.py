import json
import random
from pathlib import Path

ORDER = 3
END_TOKEN = "<END>"
MODELS_DIR = Path("data/markov_data")


def build_markov_model(names: list[str]) -> dict:
    if not names:
        raise ValueError("Empty list")
    model = {
        "order": ORDER,
        "avg_length": 0,
        "starts": {},
        "transitions": {}
    }
    transitions = model["transitions"]
    starts = model["starts"]
    total_length = 0
    valid_names = 0
    for name in names:
        name = name.lower()
        if len(name) < ORDER:
            continue
        total_length += len(name)
        valid_names += 1
        start_key = name[:ORDER]
        starts[start_key]=starts.setdefault(start_key, 0) + 1
        for i in range(len(name) - ORDER):
            key = name[i:i+ORDER]
            next_char = name[i+ORDER]
            node = transitions.setdefault(key, {})
            node[next_char] = node.setdefault(next_char, 0) + 1
        last_key = name[-ORDER:]
        node = transitions.setdefault(last_key, {})
        node[END_TOKEN] = node.setdefault(END_TOKEN, 0) + 1

    if valid_names == 0:
        raise ValueError("No names are long enough to build the model!")
    model["avg_length"] = total_length / valid_names
    return model 

def serialize_model(model: dict) -> dict:
    serialized_model = {
        "order": model["order"],
        "avg_length": model["avg_length"],
        "starts": model["starts"],
        "transitions": {}
    }
    for key, value in model["transitions"].items():
        serialized_model["transitions"][key] = value
    return serialized_model

def deserialize_model(model:dict) -> dict:
    deserialized_model = {
        "order": model["order"],
        "avg_length": model["avg_length"],
        "starts": model["starts"],
        "transitions": {}
    }   
    for key, value in model["transitions"].items():
        deserialized_model["transitions"][key] = value
    return deserialized_model

def save_model(model: dict, path: Path) -> None:
    serialized_model = serialize_model(model)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(serialized_model, file, ensure_ascii=False, indent=4)

def load_model(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        loaded_dict = json.load(file)
    deserialized_model = deserialize_model(loaded_dict)
    return deserialized_model


def get_model_path(race: str, gender: str) -> Path:
    return MODELS_DIR / f"{race}_{gender}.json"

def capitalize_name(name: str) -> str:
    if not name:
        return name
    result = []
    capitalize_next = True
    for char in name:
        if capitalize_next and char.isalpha():
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)
        if char in ("'", "-"):
            capitalize_next = True
    return "".join(result)

def markov_generate(model: dict, rng: random.Random | None = None) -> str:
        if rng is None:
            rng = random.Random()
        starts = model["starts"]
        start_population = list(starts.keys())
        start_weights = list(starts.values())
        last_name = ""
        avg_length = model["avg_length"]
        min_length = max(ORDER, int(avg_length - 2))
        max_length = int(avg_length + 2)
        for attempt in range(10):
            start = rng.choices(population=start_population, weights=start_weights, k=1)[0]
            current = start
            name = start
            while True:
                transitions = model["transitions"][current]
                transition_population = list(transitions.keys())
                transition_weights = list(transitions.values())

                next_char = rng.choices(population=transition_population, weights=transition_weights, k=1)[0]
                if next_char == END_TOKEN:
                    if len(name) >= min_length:
                        return capitalize_name(name)
                    last_name = name
                    break
                name += next_char
                current = name[-ORDER:]
                if len(name) >= max_length:
                    return capitalize_name(name)
        return capitalize_name(last_name)
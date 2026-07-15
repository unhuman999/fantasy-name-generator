import random

def generate_name(race, gender, races_data, rng: random.Random | None = None) -> str:
    if rng is None:
        rng = random.Random()
    names = races_data[race][gender]
    if len(names) == 0:
        raise ValueError(f"No names available for the race '{race}' and gender '{gender}'.")
    return rng.choice(names)

def random_names(race, gender, races_data, rng: random.Random | None = None,) -> tuple:
    if rng is None:
        rng = random.Random()
    names = races_data[race][gender]
    if len(names) < 2:
        raise ValueError(f"Not enough names for the race '{race}' and gender '{gender}'.")

    name1, name2 = rng.sample(names, 2)
    return name1, name2

def generate_hybrid_name(name1: str, name2:str) -> str:
    prefix = name1[:len(name1)//2]
    suffix = name2[len(name2)//2:]
    return (prefix+suffix).capitalize()


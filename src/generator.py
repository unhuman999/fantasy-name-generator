import json, random




def random_names(race, gender, races_data) -> tuple:
    name1, name2 = random.sample(races_data[race][gender], 2)
    return (name1, name2)

def generate_hybrid_name(name1: str, name2:str) -> str:
    prefix = name1[:len(name1)//2]
    suffix = name2[len(name2)//2:]
    return (prefix+suffix).capitalize()


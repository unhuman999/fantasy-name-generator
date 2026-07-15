import json
from pydantic import ValidationError
import sys
from src.utils import load_dataset
from src.generator import random_names, generate_hybrid_name, generate_name

def get_race(races):
    while True:
        user_races_input = input("Choose a race (Orc, Elf, Dwarf or Human): ").lower()
        if user_races_input in races:
            return user_races_input
        print("Race not defined, choose correct race from list Orc, Human, Elf, Dwarf:")

def get_gender(chosen_race, races_data):
    while True:
        user_gender_input = input("What about gender? ").lower()
        if user_gender_input in races_data[chosen_race]:
            return user_gender_input
        print("Choose correct gender(male/female):")

def get_mode():
    print("\nChoose generation mode:")
    print("1. Take an authentic name from the database")
    print("2. Create a unique hybrid name (Syllabic mix)")
    while True:
        mode = input("Enter mode number (1 or 2): ").strip()
        if mode in ("1", "2"):
            return mode
        print("Choose correct mode please")
            







if __name__ == "__main__":
    try:
        races_dataset = load_dataset("data/races_dataset.json")
    except FileNotFoundError as e:
        print(f'Warning, {e}, there is no file with dataset')
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f'Warning, {e}, bad syntax or empty string')
        sys.exit(1)
    except ValidationError as e:
        print(f'Warning, {e}, dataset validation failed')
        sys.exit(1)

    user_target_race = get_race(races_dataset)
    user_target_gender = get_gender(user_target_race, races_dataset)

    mode = get_mode()
    try:
        if mode == "2": 
            n1, n2 = random_names(user_target_race, user_target_gender, races_dataset)
            generated_name = generate_hybrid_name(n1, n2) 
            print(f"\n[Hybrid Mode] Original blueprints: {n1} + {n2}")
        else:
            generated_name=generate_name(user_target_race, user_target_gender, races_dataset)
            print(f"\n[Classic Mode]")
    except ValueError as e:
        print(f'Warning, {e}, not  enough names')
        sys.exit(1)
    print(f"Generated Name: {generated_name}")


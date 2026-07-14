import random
import sys
from src.utils import load_dataset
from src.generator import random_names, generate_hybrid_name

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



def generate_name(race, gender, races_data):
    return random.choice(races_data[race][gender])





if __name__ == "__main__":
    races_dataset = load_dataset("data/races_dataset.json")
    if not races_dataset:
        print(f'Ошибка, исходный словарь пустой')
        sys.exit()

    user_target_race = get_race(races_dataset)
    user_target_gender = get_gender(user_target_race, races_dataset)
    print("\nChoose generation mode:")
    print("1. Take an authentic name from the database")
    print("2. Create a unique hybrid name (Syllabic mix)")
    mode = input("Enter mode number (1 or 2): ").strip()

    if mode == "2":
        n1, n2 = random_names(user_target_race, user_target_gender, races_dataset)
        generated_name = generate_hybrid_name(n1, n2)
        print(f"\n[Hybrid Mode] Original blueprints: {n1} + {n2}")
    else:
        generated_name=generate_name(user_target_race, user_target_gender, races_dataset)
        print(f"\n[Classic Mode]")
    print(f"Generated Name: {generated_name}")


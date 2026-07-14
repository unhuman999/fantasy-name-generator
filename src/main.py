import random
import sys
from src.utils import load_dataset

def get_race(races):
    while True:
        user_races_input = input("Choose a race (orc, elf, or human): ").lower()
        if user_races_input in races:
            return user_races_input
        print("Race not defined, choose correct race from list Orc, Human, Elf:")

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
    generated_name=generate_name(user_target_race, user_target_gender, races_dataset)
    print(generated_name)


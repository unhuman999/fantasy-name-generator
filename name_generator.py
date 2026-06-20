import random

races = {
    "orc":{
        "male":["Azgoth", "Borgakh", "Durgash", "Grommash", "Khazuk", "Mogdurz", "Nagrul", "Ruggoth", "Thokrak", "Uzgash"],
        "female":["Agtha", "Borga", "Duhgasha", "Gorshka", "Khagra", "Lagak", "Mugra", "Nagra", "Sharga", "Urzga"]
    },
    "elf":{
        "male":["Aelar", "Thalanil", "Faelivrin", "Kaelen", "Ornthalas", "Rielan", "Sildor", "Theron", "Valandris", "Zylarien"],
        "female":["Aelindel", "Celethiel", "Elowen", "Faeruna", "Laeral", "Merilwen", "Nimphiel", "Sariel", "Thaviel", "Yavanna"]
    },
    "human":{
        "male":["Aldric", "Brennan", "Corvin", "Darian", "Evander", "Gregor", "Haldric", "Loric", "Randver", "Theron"],
        "female":["Adara", "Brigid", "Caelia", "Elara", "Gwendolyn", "Isolde", "Linette", "Rosamund", "Seren", "Theodora"]
    }
}




def get_race():
    while True:
        user_info1 = input("What race name do you want to generate(orc, elf or human)? ").lower()
        if user_info1 in races:
            return user_info1
        print("Race not defined, choose correct race from list Orc, Human, Elf:")
    
def get_gender(race):
    while True:
        user_info2 = input("What about gender?").lower()
        if user_info2 in races[race]:
            return user_info2
        print("Choose correct gender(male/female):")
    

# while True:
#     user_target_race = input("What race name do you want to generate(orc, elf or human)? ").lower()
#     if user_target_race in races:
#         break
#     print("Race not defined, choose correct race from list Orc, Human, Elf:")

# while True:
#     user_target_gender = input("What about gender?").lower()
#     if user_target_gender in races[user_target_race]:
#         break
#     print("Choose correct gender(male/female):")

user_target_race = get_race()
user_target_gender = get_gender(user_target_race)

def generate_name(race, gender):
    return random.choice(races[race][gender])

generated_name = generate_name(user_target_race, user_target_gender)

print(generated_name)



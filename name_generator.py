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



def show_names(names):
    for name in names:
        print(name)
def count_names(names):
    print(f"Total: {len(names)}")
def race_info(names):
    show_names(names)
    count_names(names)

####Now freezed
##race_info(races["orc"]["male"])
##race_info(races["orc"]["female"])
##race_info(races["elf"]["male"])
##race_info(races["elf"]["female"])
##race_info(races["human"]["male"])
##race_info(races["human"]["female"])

user_target_race = input("What race name do you want to generate(orc, elf or human)?").lower()
user_target_gender = input("What about gender?").lower()



print(random.choice(races[user_target_race][user_target_gender]))
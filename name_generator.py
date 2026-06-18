orc_male = ["Azgoth", "Borgakh", "Durgash", "Grommash", "Khazuk", "Mogdurz", "Nagrul", "Ruggoth", "Thokrak", "Uzgash"]
orc_female = ["Agtha", "Borga", "Duhgasha", "Gorshka", "Khagra", "Lagak", "Mugra", "Nagra", "Sharga", "Urzga"]
elf_male = ["Aelar", "Thalanil", "Faelivrin", "Kaelen", "Ornthalas", "Rielan", "Sildor", "Theron", "Valandris", "Zylarien"]
elf_female = ["Aelindel", "Celethiel", "Elowen", "Faerûna", "Laeral", "Merilwen", "Nimphiel", "Sariel", "Thaviel", "Yavanna"]
human_male = ["Aldric", "Brennan", "Corvin", "Darian", "Evander", "Gregor", "Haldric", "Loric", "Randver", "Theron"]
human_female = ["Adara", "Brigid", "Caelia", "Elara", "Gwendolyn", "Isolde", "Linette", "Rosamund", "Seren", "Theodora"]
def show_names(names):
    for name in names:
        print(name)
def count_name(names):
    print(f"Total: {len(names)}")
def race_info(names):
    show_names(names)
    count_name(names)
race_info(orc_male)
race_info(orc_female)
race_info(elf_male)
race_info(elf_female)
race_info(human_male)
race_info(human_female)
# Créé par tom.deboskre, le 02-12-2021 en Python 3.7
#exo3

first_name = input("quel est ton prénom?")
first_name2 = ""

for lettre in first_name:
    first_name2=lettre + first_name2

print (first_name2)
# Créé par tom.deboskre, le 06-12-2021 en Python 3.7

Nombre1 = input("quel est votre premier nombre ")
Nombre2 = input("quel est votre deuxieme nombre ")

operation = input("quel operations voulez vous faire ?\n[1] addition\n[2] soustrations\n[3] multiplication\n[4] division\n ")
operator = ""
total = 0 

if operation == "1" :
    total = int(Nombre1) + int(Nombre2)
    operator = "+"

if operation == "2" :
    total = int(Nombre1) - int(Nombre2)
    operator = "-"

if operation == "3" :
    total = int(Nombre1) * int(Nombre2)
    operator = "*"

if operation == "4" :
    total = int(Nombre2) / int(Nombre2)
    operator = "/"

print("voici le resultat : " + str(Nombre1) + " " + str(operator) + " "  + str(Nombre2) + " = " + str(total) )
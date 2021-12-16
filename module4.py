# Créé par tom.deboskre, le 02-12-2021 en Python 3.


prenom = input("quel est ton prénom? ")
nom = input("quel est ton nom? ")
anneenaissance = input("quel est ton année de naissance? ")
annee = float(2021)
age= annee-float(anneenaissance)

print("Bienvenue " + prenom + " " + nom + " tu a "+ str(age) + " ans!")
# %%
# Exercice 1

'''
Description de l'exercice:
Écrire un script Python qui demande un nombre à l'utilisateur et affiche s'il est positif, négatif ou nul.
'''
nombre = input("Entrez un nombre!")

if nombre == 0:
    print("Votre nombre: ", nombre, "est nul!")
elif nombre > 0:
    print("Votre nombre: ", nombre, "est positif!")
else:
    print("Votre nombre: ", nombre, "est négatif!")

# %%
# Exercice 2

'''
Description de l'exercice:
Créer un script qui demande l'âge de l'utilisateur et affiche s'il est majeur ou mineur.
'''
age= int(input("Entrez votre âge!"))
if age>=18:
    print("Vous êtes majeur!")
else:
    print("Vous êtes mineur!")

# %%
# Exercice 3

'''
Description de l'exercice:
Écrire un script qui prend trois nombres en entrée et affiche le plus grand des trois.
'''
nombre1 = int(input("Entrez le premier nombre!"))       
nombre2 = int(input("Entrez le deuxième nombre!"))
nombre3 = int(input("Entrez le troisième nombre!"))

if nombre1 > nombre2 and nombre1 > nombre3:
    print("Le plus grand nombre est: ", nombre1)
elif nombre2 > nombre1 and nombre2 > nombre3:
    print("Le plus grand nombre est: ", nombre2)
else:
    print("Le plus grand nombre est: ", nombre3)
    
# %%
# Exercice 4

'''
Description de l'exercice:
Créer un script qui calcule la moyenne de trois notes et affiche si l'étudiant a réussi (moyenne >= 10).
'''

note1 = int(input("Entrez la première note!"))
note2 = int(input("Entrez la deuxième note!"))
note3 = int(input("Entrez la troisième note!"))

moyenne = (note1 + note2 + note3) / 3

if moyenne >= 10:
    print("Vous avez réussi!")
else:
    print("Vous avez échoué!")

# %%
# Exercice 5

'''
Description de l'exercice:
Écrire un script qui prend un nombre en entrée et affiche "pair" ou "impair".
'''
nombre = int(input("Entrez un nombre!"))

if nombre % 2 == 0:
    print("Votre nombre est pair!")
else:
    print("Votre nombre est impair!")


# %%
# Exercice 6

'''
Description de l'exercice:
Créer un script qui demande un mois en entrée et affiche le nombre de jours dans ce mois.
'''

mois = input("Entrez un mois!")

if mois == "janvier" or mois == "mars" or mois == "mai" or mois == "juillet" or mois == "août" or mois == "octobre" or mois == "décembre":
    print("Le mois", mois, "a 31 jours!")
elif mois == "février":
    print("Le mois", mois, "a 28 ou 29 jours!")
else:
    print("Le mois", mois, "a 30 jours!")


# %%
# Exercice 7

'''
Description de l'exercice:
Écrire un script qui simule un login : demander un nom d'utilisateur et un mot de passe, et afficher un message de bienvenue si les informations sont correctes.
'''
user=input("Entrez votre nom d'utilisateur!")
mdp = input("Entrez votre mot de passe!")

if user == "admin" and mdp == "admin":
    print("Bienvenue", user, "!")
else:
    print("Nom d'utilisateur ou mot de passe incorrect!")  


# %%
# Exercice 8

'''
Description de l'exercice:
Créer un script qui demande une année et affiche si elle est bissextile ou non.
'''

annee= int(input("Entrez une année!"))

if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
    print("L'année", annee, "est bissextile!")
else:
    print("L'année", annee, "n'est pas bissextile!")


# %%
# Exercice 9

'''
Description de l'exercice:
Écrire un script qui demande deux nombres et affiche "Plus grand", "Plus petit" ou "Égal" selon leur comparaison.
'''

nombre1 = int(input("Entrez le premier nombre!"))
nombre2 = int(input("Entrez le deuxième nombre!"))

if nombre1 > nombre2:
    print("Le premier nombre est plus grand!")
elif nombre1 < nombre2:
    print("Le deuxième nombre est plus grand!")
else:
    print("Les deux nombres sont égaux!")


# %%
# Exercice 10

'''
Description de l'exercice:
Créer un script qui prend un nombre entier et affiche si ce nombre est divisible par 5 et 10.
'''

nombre = int(input("Entrez un nombre!"))

if nombre % 5 == 0 and nombre % 10 == 0:
    print("Votre nombre est divisible par 5 et 10!")
else:
    print("Votre nombre n'est pas divisible par 5 et 10!")

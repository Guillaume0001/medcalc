from depencies import mbasal
from depencies import imc
from depencies import verification
import time
import shutil

pycache = "./depencies/__pycache__"
shutil.rmtree(pycache)

print("+-------------------------------------------------------------------+")
print(f"|                          MEDCALC PROGRAM                          |")
print(f"|  Calculateur d'IMC et de Métabolisme Basal (Métabolisme de Base)  |")
print(f"|              Sous Licence MIT - Tous droits réservés              |")
print(f"|              Développé et crée par Guillaume MALEYRAT             |")
print(f"+-------------------------------------------------------------------+")
print("\n")

verification.main()
verification.depencies()

print(f"Calcul disponible:")
print(f"Pour le métabolisme basal, entrez 1;")
print(f"Pour le index de masse du corps entrez 2;")
print(f"")
option = input("Quelle option choisissez vous ? Veuillez entrer l'un des chiffres cités ci-dessus.\n > ")
print(f"")

if int(option) == 1:
    print(f"Type de calcul:")
    print(f"Si le patient est un homme, entrez 1;")
    print(f"Si le patiente est une femme, entrez 2;")
    option = input("Quelle option choisissez vous ? Veuillez entrer l'un des chiffres cités ci-dessous.\n > ")
    print(f"")
    if int(option) == 1:
        print(f"Calcul du Métabolisme Basal pour un patient de sexe masculin choisi.")
        poids = input("Poids du patient (kg).\n > ")
        taille = input("Taille du patient (m).\n > ")
        age = input("Age du patient.\n > ")
        mbasal.homme(poids, taille, age)
        print(f"Merci d'avoir utilisé mon logiciel ! L'application se fermera automatiquement dans deux minutes.")
        time.sleep(120)
        print(f"Bonne journée !")
        exit()
    elif int(option) == 2:
        print(f"Calcul du Métabolisme Basal pour un patient de sexe féminin choisi.")
        poids = input("Poids de la patiente (kg).\n > ")
        taille = input("Taille de la patiente (m).\n > ")
        age = input("Age de la patiente.\n > ")
        mbasal.femme(poids, taille, age)
        print(f"Merci d'avoir utilisé mon logiciel ! L'application se fermera automatiquement dans deux minutes.")
        time.sleep(120)
        print(f"Bonne journée !")
        exit()
    else:
        print(f"Erreur ! Le chiffre / nombre entrée est incorrect !")
elif int(option) == 2:
    print(f"Type de calcul:")
    print(f"Si le patient est un homme, entrez 1;")
    print(f"Si le patient est une femme, entrez 2;")
    option = input("Quelle option choisissez vous ? Veuillez entrer l'un des chiffres cités ci-dessous.\n > ")
    print(f"")
    if int(option) == 1:
        print(f"Calcul de l'IMC pour un patient de sexe masculin choisi.")
        poids = input("Poids du patient (kg).\n > ")
        taille = input("Taille du patient (m).\n > ")
        imc.homme(poids, taille)
        print(f"Merci d'avoir utilisé mon logiciel ! L'application se fermera automatiquement dans deux minutes.")
        time.sleep(120)
        print(f"Bonne journée !")
        exit()
    elif int(option) == 2:
        print(f"Calcul de l'IMC pour un patient de sexe féminin choisi.")
        poids = input("Poids de la patiente (kg).\n > ")
        taille = input("Taille de la patiente (m).\n > ")
        imc.femme(poids, taille)
        print(f"Merci d'avoir utilisé mon logiciel ! L'application se fermera automatiquement dans deux minutes.")
        time.sleep(120)
        print(f"Bonne journée !")
        exit()
    else:
        print(f"Erreur ! Le chiffre / nombre entrée est incorrect !")
else:
    print(f"Erreur ! Le chiffre / nombre entrée est incorrect !")
    print(f"L'application se fermera automatiquement dans deux minutes.")
    time.sleep(120)
    exit()
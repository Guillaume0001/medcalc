import requests
import os
import time

def version():
    version_file = "version.txt"
    online_file = "https://raw.githubusercontent.com/Guillaume0001/medcalc/main/version.txt"
    request = requests.get(online_file)
    if request.status_code == 200:
        online_version = request.content.decode('utf-8')
    else:
        online_version = "Unknown"

    if not os.path.exists(version_file):
        print(f"Erreur ! Le fichier de version n'existe pas...")
    
    with open(version_file, 'r', encoding='utf-8') as version_file:
        local_version = version_file.read().strip()
    
    if local_version != online_version:
        print(f"Erreur ! La version du logiciel est incorrect !")
        print(f"Version du logiciel installé: " + local_version)
        print(f"Version du logiciel en ligne: " + online_version)
    else:
        print(f"Logiciel à jour...")

def main():
    main_file = "main.py"
    online_file = "https://raw.githubusercontent.com/Guillaume0001/medcalc/main/main.py"
    request = requests.get(online_file)
    if request.status_code == 200:
        online_file = request.content.decode('utf-8')
    else:
        online_file = "Unknown"
    
    with open(main_file, 'r', encoding='utf-8') as main_file:
        local_file = main_file.read().strip()
    
    if local_file != online_file:
        print(f"Erreur ! L'intégrité du logiciel est modifié...")
        print(f"Le logiciel est bloqué, veuillez contacter notre équipe: guillaume.m@liberagroup.fr")
        time.sleep(120)
        exit()

def depencies():
    path_depencies = "depencies/imc.py"
    online_file = "https://raw.githubusercontent.com/Guillaume0001/medcalc/main/depencies/imc.py"
    request = requests.get(online_file)
    if request.status_code == 200:
        online_file = request.content.decode('utf-8')
    else:
        online_file = "Unknown"
    
    with open(path_depencies, 'r', encoding='utf-8') as depencies_file:
        local_file = depencies_file.read().strip()
    
    if local_file != online_file:
        print(f"Erreur ! L'intégrité du logiciel est modifié...")
        print(f"Le logiciel est bloqué, veuillez contacter notre équipe: guillaume.m@liberagroup.fr")
        time.sleep(120)
        exit()
    
    path_depencies = "depencies/mbasal.py"
    online_file = "https://raw.githubusercontent.com/Guillaume0001/medcalc/main/depencies/mbasal.py"
    request = requests.get(online_file)
    if request.status_code == 200:
        online_file = request.content.decode('utf-8')
    else:
        online_file = "Unknown"
    
    with open(path_depencies, 'r', encoding='utf-8') as depencies_file:
        local_file = depencies_file.read().strip()
    
    if local_file != online_file:
        print(f"Erreur ! L'intégrité du logiciel est modifié...")
        print(f"Le logiciel est bloqué, veuillez contacter notre équipe: guillaume.m@liberagroup.fr")
        time.sleep(120)
        exit()

    path_depencies = "depencies/verification.py"
    online_file = "https://raw.githubusercontent.com/Guillaume0001/medcalc/main/depencies/verification.py"
    request = requests.get(online_file)
    if request.status_code == 200:
        online_file = request.content.decode('utf-8')
    else:
        online_file = "Unknown"
    
    with open(path_depencies, 'r', encoding='utf-8') as depencies_file:
        local_file = depencies_file.read().strip()
    
    if local_file != online_file:
        print(f"Erreur ! L'intégrité du logiciel est modifié...")
        print(f"Le logiciel est bloqué, veuillez contacter notre équipe: guillaume.m@liberagroup.fr")
        time.sleep(120)
        exit()
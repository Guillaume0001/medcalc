def homme(p, t):
    calcul = float(p)/(float(t)*float(t))
    ct = str(p) + " / " + str(t) + " * " + str(t)
    result = calcul
    print(f"Calcul en cours...")
    print(f"La calcul pour le patient est: " + str(ct) + ".")
    print(f"Le résultat du calcul ci-dessus est approximativement: " + str(result) + ".")
    print(f"")
    print(f"Soit, le patient a un IMC de " + str(result) + ".")

def femme(p, t):
    calcul = float(p)/(float(t)*float(t))
    ct = str(p) + " / " + str(t) + " * " + str(t)
    result = calcul
    print(f"Calcul en cours...")
    print(f"La calcul pour la patiente est: " + str(ct) + ".")
    print(f"Le résultat du calcul ci-dessus est approximativement: " + str(result) + ".")
    print(f"")
    print(f"Soit, la patiente a un IMC de " + str(result) + ".")
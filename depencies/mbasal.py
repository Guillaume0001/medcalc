def homme(p, t, a):
    calcul = (13.707*float(p))+(492.3*float(t))-(6.673*float(a))+77.607
    ct = "(13,707*" + str(p) + ") + (492,3*" + str(t) + ") - (6,673*" + str(a) + ") + 77.607"
    result = calcul
    print(f"Calcul en cours...")
    print(f"Le calcul pour le patient est: " + str(ct))
    print(f"Le résultat du calcul ci-dessus est approximativement: " + str(result) + ".")
    print(f"")
    print(f"Soit, le patient a un métabolisme de base de " + str(result) + ".")

def femme(p, t, a):
    calcul = (9.740*float(p))+(172.9*float(t))-(4.737*float(a))+667.051
    ct = "(13,707*" + str(p) + ") + (492,3*" + str(t) + ") - (6,673*" + str(a) + ") + 77.607"
    result = calcul
    print(f"Calcul en cours...")
    print(f"Le calcul pour la patiente est: " + str(ct))
    print(f"Le résultat du calcul ci-dessus est approximativement: " + str(result) + ".")
    print(f"")
    print(f"Soit, le patient a un métabolisme de base de " + str(result) + ".")
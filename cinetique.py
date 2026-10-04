import math

#--------Partie 1 : Calcul de la concentration --------#

def calculer_concentration(Ci, k, t):
    """
    Cette fonction calcule la concentration finale (Cf) en utilisant la formule :
    Cf = Ci * e^(-k * t)

    Paramètres :
    Ci : concentration initiale (mg/L)
    k : constante empirique (L/(mg*min))
    t : temps (min)

    Valeur retournée :
    La valeur que l'on a retournée est la concentration finale (Cf) en mg/L.
    """
    if Ci < 0:
        raise ValueError("La concentration initiale (Ci) ne peut pas être négative.")
    if k <= 0:
        raise ValueError("La constante empirique (k) doit être positive.")
    if t < 0:
        raise ValueError("Le temps (t) ne peut pas être négatif.")

    return Ci * math.exp(-k * t)

#--------Partie 2 : Simulation de l'évolution de la concentration --------#

def calculer_demi_vie(k):
    """
    Cette fonction calcule la demi-vie (t_demi_vie) en utilisant la formule :
    t_demi_vie = (ln(2) / k)

    Paramètres :
    k : constante empirique (L/(mg*min))

    Valeur retournée :
    La demi-vie (min).
    """
    if k <= 0:
        raise ValueError("La constante empirique (k) doit être positive.")

    return math.log(2) / k

#--------Partie 3 : Conversion d'unités --------#

def convertir_concentration(valeur, unité_source, unité_cible):
    """
    Cette fonction convertit une concentration entre mg/L et µg/mL.
    """
    source = unité_source.strip().replace("µ", "u").replace("μ", "u")
    cible = unité_cible.strip().replace("µ", "u").replace("μ", "u")
    unités_valides = {"mg/L", "ug/mL"}

    if source not in unités_valides:
        raise ValueError("Les unités fournies sont invalides. Elles doivent être en mg/L ou µg/mL !")
    if cible not in unités_valides:
        raise ValueError("Les unités fournies sont invalides. Elles doivent être en mg/L ou µg/mL !")
    if source == cible:
        return valeur

    if (source == "mg/L" and cible == "ug/mL") or (source == "ug/mL" and cible == "mg/L"):
        return valeur

    raise ValueError("Conversion non supportée pour ces unités.")

#--------Partie 4 : Évaluation du niveau réactionnel --------#

def evaluer_niveau(concentration, seuil_min, seuil_max):
    """
    Cette fonction évalue le niveau réactionnel (v) selon la concentration.
    """
    if seuil_min >= seuil_max:
        raise ValueError("Le seuil minimum doit être inférieur au seuil maximum.")
    if concentration < seuil_min:
        return "INSUFFISANT"
    if concentration <= seuil_max:
        return "OPTIMAL"
    return "TOXIQUE / CRITIQUE"

#--------Partie 5 : Simulation de l'évolution de la concentration --------#

def main():
    Ci = float(input("Entrez la concentration initiale (Ci) en mg/L : "))
    k = float(input("Entrez la constante empirique (k) en L/(mg*min) : "))
    t = float(input("Entrez le temps (t) en minutes : "))

    Cf = calculer_concentration(Ci, k, t)
    print("La concentration finale est de : ", round(Cf, 4), " mg/L")

    t_demi_vie = calculer_demi_vie(k)
    print("La demi-vie est de : ", round(t_demi_vie, 4), "minutes")

    unité_source = input("Entrez l'unité source (mg/L ou µg/mL) : ").strip()
    unité_cible = input("Entrez l'unité cible (mg/L ou µg/mL) : ").strip()
    valeur_convertie = convertir_concentration(Cf, unité_source, unité_cible)
    print(f"Valeur convertie : {round(valeur_convertie, 4)} {unité_cible}")

    seuil_min = float(input("Entrez le seuil minimum pour la concentration initiale (mg/L) : "))
    seuil_max = float(input("Entrez le seuil maximum pour la concentration initiale (mg/L) : "))
    niveau = evaluer_niveau(Cf, seuil_min, seuil_max)
    print("Niveau évalué : ", niveau)


if __name__ == "__main__":
    main()


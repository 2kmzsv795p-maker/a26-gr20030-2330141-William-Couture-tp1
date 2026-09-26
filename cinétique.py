 #-------Partie 1 : Calcul de la concentration finale ( Cf ) --------#

import math

Ci= float(input("Entrez la concentration initiale (Ci) en mg/L : "))  #Demande d'entrer la concentration initiale
k= float(input("Entrez la constante empirique (k) en L/(mg*min) : "))  #Demande d'entrer la constante empirique
t= float(input("Entrez le temps (t) en minutes : "))  #Demande d'entrer le temps        

def calculer_concentration_finale(Ci, k, t):

    """
    Cette fonction calcule la concentration finale (Cf) en utilisant la formule :
    Cf = Ci * e^(-k * t)
    
    Paramètres :
    Ci : concentration initiale (mg/L)
    k : constante empirique (L/(mg*min))
    t : temps (min)
    
    Valeur retournée :
    La valeur que l'on a retournée est la concentration finale (Cf) en mg/L.:
    Cf : concentration finale (mg/L)
    """
    if Ci < 0 :
        raise ValueError("La concentration initiale (Ci) ne peut pas être négative.")       
    if k <= 0 :
        raise ValueError("La constante empirique (k) doit être positive.")
    if t < 0 :
        raise ValueError("Le temps (t) ne peut pas être négatif.")
    
    return Ci * math.exp(-k * t)  #Calcul de la concentration finale en utilisant la formule donnée

Cf = calculer_concentration_finale(Ci, k, t)
print("La concentration finale est de : ", round(Cf,4), " mg/L")

#--------Partie 2 : Calcul de la demi vie ( t_demi_vie ) --------#

def calculer_la_demi_vie(k):

    """
    Cette fonction calcule la demi-vie (t_demi_vie) en utilisant la formule :
    t_demi_vie = (ln(2) / k)
    
    Paramètres :
    k : constante empirique (L/(mg*min))
    
    Valeur retournée :
    La valeur que l'on a retournée est la demi-vie (t_demi_vie) en minutes.:
    t_demi_vie : demi-vie (min)
    """
    if k <= 0 :
        raise ValueError("La constante empirique (k) doit être positive.")
    
    return math.log(2) / k  #Calcul de la demi-vie en utilisant la formule donnée   

t_demi_vie =calculer_la_demi_vie(k)
print("La demi-vie est de : ", round(t_demi_vie ,4), "minutes")


#--------Partie 3 : Conversion de concentration entre unités --------#

unité_source = input("Entrez l'unité source (mg/L ou µg/mL) : ").strip()
unité_cible = input("Entrez l'unité cible (mg/L ou µg/mL) : ").strip()

def convertir_concentration(valeur, unité_source, unité_cible):
    """
    Cette fonction convertit une concentration entre mg/L et µg/mL.

    Paramètres :
    valeur : la valeur de la concentration à convertir
    unité_source : l'unité de la concentration source (mg/L ou µg/mL)
    unité_cible : l'unité de la concentration cible (mg/L ou µg/mL)

    Valeur retournée :
    La valeur de la concentration convertie dans l'unité cible.
    """
    source = unité_source.replace("µ", "u")
    cible = unité_cible.replace("µ", "u")
    unités_valides = {"mg/L", "ug/mL"}

    if source not in unités_valides:
        raise ValueError("Les unités fournies sont invalides. Elles doivent être en mg/L ou µg/mL !")
    if cible not in unités_valides:
        raise ValueError("Les unités fournies sont invalides. Elles doivent être en mg/L ou µg/mL !")
    if source == cible:
        return valeur

    # 1 mg/L = 1 µg/mL
    if (source == "mg/L" and cible == "ug/mL") or (source == "ug/mL" and cible == "mg/L"):
        return valeur

    raise ValueError("Conversion non supportée pour ces unités.")

valeur_convertie = convertir_concentration(Cf, unité_source, unité_cible)
print(f"Valeur convertie : {round(valeur_convertie, 4)} {unité_cible}")

#--------Partie 4 : Calcul de la vitesse de réaction ( v ) --------#

seuil_min = float(input("Entrez le seuil minimum pour la concentration initiale (mg/L) : "))
seuil_max = float(input("Entrez le seuil maximum pour la concentration initiale (mg/L) : "))
    
def evaluer_niveau (concentration, seuil_min, seuil_max):
    """
    Cette fonction évalue le niveau réactionnel (v) en utilisant la formule :
    v = (Ci - Cf) / t
    
    Paramètres :
    Ci : concentration initiale (mg/L)
    Cf : concentration finale (mg/L)
    t : temps (min)
    seuil_min : seuil minimum pour la concentration initiale (mg/L)
    seuil_max : seuil maximum pour la concentration initiale (mg/L) 

    Valeur retournée :
    La valeur que l'on a retournée est la vitesse de réaction (v) en mg/(L*min).
    La chaine de caractères qui contient :
     "INSUFFISANT" si C < seuil_min
     "OPTIMAL" si seuil_min <= C <= seuil_max
     "TOXIQUE / CRITIQUE" si C > seuil_max

    """
    if seuil_min >= seuil_max:
        raise ValueError("Le seuil minimum doit être inférieur au seuil maximum.")
    if concentration < seuil_min:
        return "INSUFFISANT"
    elif concentration <= seuil_max:
        return "OPTIMAL"
    else:
        return "TOXIQUE / CRITIQUE" 

niveau = evaluer_niveau(Cf, seuil_min, seuil_max)
print("Niveau évalué : ", niveau)


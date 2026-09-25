#Première étape pour bien comprendre comment la formule fonctionne et faire quelques tests pour tester le code initiale.

import math    #vue que l'on utilise la fonction exponentielle, on importe le module math  
Ci= float(input("Entrez la concentration initiale (Ci) en mg/L : "))  #Demande à l'utilisateur d'entrer la concentration initiale
k= float(input("Entrez la constante empirique (k) en L/(mg*min) : "))  #Demande à l'utilisateur d'entrer la constante empirique
t= float(input("Entrez le temps (t) en minutes : "))  #Demande à l'utilisateur d'entrer le temps        

def calculer_concentration_finale(Ci, k, t):

    """
    Cette fonction calcule la concentration finale (Cf) en utilisant la formule :
    Cf = Ci * e^(-k * t)
    
    Paramètres :
    Ci : concentration initiale (mg/L)
    k : constante empirique (L/(mg*min))
    t : temps (min)
    
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
#print("La concentration finale est de : ", round(Cf,4), " mg/L")

print("La concentration finale est de : ", round(Cf,4), " mg/L")

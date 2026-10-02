from cinétique import calculer_concentration
from cinétique import calculer_demi_vie

#--------Partie 5 : Simulation de l'évolution de la concentration --------#
def simuler_evolution(c0, k, durée_heures):
    """
    Cette fonction simule l'évolution de la concentration à chaque heure
    en utilisant la formule : C(t) = C0 * e^(-k * t)
    """
    if c0 <= 0:
        raise ValueError("La concentration initiale (c0) doit être positive.")
    if k <= 0:
        raise ValueError("La constante de dégradation (k) doit être positive.")
    if durée_heures <= 0:   # on n'a pas le choix d'avoir une durée positive, sinon on ne peut pas faire de simulation.
        raise ValueError("La durée (durée_heures) doit être positive.")

    concentrations = []    # ici , on va pouvoir ajouter nos valeur dans notre liste

    for heure in range(durée_heures + 1):    # cela nous permet d'ajouter une heure et de vraiment avoir un liste ou chaque valeur est suivi d'une valeur ou la concentration est 1h plus tard et d'inclure t=0 dans la simulation.
     c = calculer_concentration(c0, k, heure) # 'heure' est créé automatiquement par la boucle for : il prend 0,1,2,... à chaque tour.
    concentrations.append(c)     #ici, append nous permet d'ajouter les valeur de "c" dans la liste concentrations
    return concentrations


#--------Partie 6 : Analyse des résultats simulés --------#

def analyser_resultats(liste_concentrations, seuil_min, seuil_max):
    """
    Cette fonction analyse la liste de concentrations obtenue par simuler_évolution.

    Paramètres :
    liste_concentrations : liste contenant des valeurs de concentration
    seuil_min : seuil thérapeutique minimal (mg/L)
    seuil_max : seuil toxique maximal (mg/L)

    Valeur retournée :
    Une chaîne de caractères contenant :
      - La concentration maximale (Cmax)
      - Le nombre d'heures en zone OPTIMAL
    """

    if not isinstance(liste_concentrations, list):  #isinstance nous permt de valider si la valeur x est bien de type list, sinon on ne peut pas faire d'analyse sur les résultats.
        raise ValueError("Les résultats doivent être fournis dans une liste.")
    if len(liste_concentrations) == 0: # Si la liste n'a pas de valeur, on ne peut pas faire d'analyse sur les résultats.
        raise ValueError("La liste des concentrations ne peut pas être vide.")
    if seuil_min >= seuil_max:
        raise ValueError("Le seuil minimum doit être inférieur au seuil maximum.")

    for valeur in liste_concentrations:
        if not isinstance(valeur, (int, float)):
            raise ValueError("Tous les éléments de la liste doivent être des nombres.")

    concentration_maximale = max(liste_concentrations)

    heures_optimal = 0
    for c in liste_concentrations:
        if seuil_min <= c <= seuil_max:
            heures_optimal += 1

    rapport = ("Analyse des résultats\n----------------------\nConcentration maximale (Cmax) : "
               + str(concentration_maximale)
               + " mg/L\nHeures en zone OPTIMAL : "
               + str(heures_optimal)
               + "\n")

    return rapport

liste_concentrations = simuler_evolution(c0=50, k=0.1, durée_heures=10)
resultat_analyse = analyser_resultats(liste_concentrations, seuil_min=15, seuil_max=30)
print(resultat_analyse)



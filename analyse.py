from cinétique import calculer_concentration
from cinétique import calculer_demi_vie

#--------Partie 5 : Simulation de l'évolution de la concentration --------#
def simuler_évolution(c0, k, durée_heures):
    """
    Cette fonction simule l'évolution de la concentration à chaques heures en 
    en utilisant la formule :  C(t) = C0 * e^(-k * t)

    Paramètres :
    c0 : concentration initiale (mg/L), doit être > 0
    k : constante de dégradation (/h), doit être > 0
    durée_heures : durée totale de la simulation (heures), doit être > 0

    Valeur retournée :
    Une liste contenant la concentration calculée pour chaque heure,
    de t = 0 jusqu'à t = durée_heures.

    """

    if c0 <= 0:   # c0 ne peux pas être négatif, sinon la concentration va augmenter au lieu de diminuer.
        raise ValueError("La concentration initiale (c0) doit être positive.")
    if k <= 0: # la dégradation (k) ne peut pas être négatif, sinon la concentration va augmenter au lieu de diminuer.
        raise ValueError("La constante de dégradation (k) doit être positive.")
    if durée_heures <= 0:   # on n'a pas le choix d'avoir une durée positive, sinon on ne peut pas faire de simulation.
        raise ValueError("La durée (durée_heures) doit être positive.")

    concentrations = []    # ici , on va pouvoir ajouter nos valeur dans notre liste

    for heure in range(durée_heures + 1):    # cela nous permet d'ajouter une heure et de vraiment avoir un liste ou chaque valeur est suivi d'une valeur ou la concentration est 1h plus tard et d'inclure t=0 dans la simulation.
        c = calculer_concentration(c0, k, heure) # 'heure' est créé automatiquement par la boucle for : il prend 0,1,2,... à chaque tour.
        concentrations.append(c)     #ici, append nous permet d'ajouter les valeur de "c" dans la liste concentrations

    return concentrations



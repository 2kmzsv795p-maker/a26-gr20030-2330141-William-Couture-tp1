#Première étape pour bien comprendre comment la formule fonctionne et faire quelques tests pour tester le code initiale.

import math    #vue que l'on utilise la fonction exponentielle, on importe le module math  

""" Nous allons demander à l'utilisateur d'entrer les valeurs de la concentration initiale, de la constante empirique et du temps pour calculer la concentration finale."""
""" Nous allon sensuite faire rouler le programme et voir avec les valeurs entrées si le programme fonctionne correctement et si la concentration finale est correcte."""
""" Si les values entrées ne sont pas correctes, le programme va afficher un message d'erreur et demander à l'utilisateur de rentrer une nouvelle valeur en prenant compte des contraintes."""

Ci = float(input("Entrer la concentration intiale (mg/L) : ")) #concentration intitiale en mg/L
if Ci <= 0.5:
    print("La concentration initiale n'est pas assez élevée, prenez une valeur plus grande que 0,5 mg/L s'il vous plaît")
elif Ci >= 10:
    print ("La concentration initiale est trop élevée, prenez une valeur plus petite que 10 mg/L s'il vous plaît")
else:
    print("La concentration initiale est correcte")

k = float(input("Entrer la constante empirique (L/(mg*min)) : ")) #constante empirique
if k <= 0.1:
    print("La constante empirique n'est pas assez élevée, prenez une valeur plus grande que 0,1 L/(mg*min) s'il vous plaît")
elif k >= 2:
    print ("La constante empirique est trop élevée, prenez une valeur plus petite que 2 L/(mg*min) s'il vous plaît")
else:
    print("La constante empirique est correcte")
    
t = float(input("Entrer le temps (min) : ")) #pour un temps donné
if t <= 0:
    print("Le temps n'est pas assez élevé, il doit minimum être au dessus de 1 minute")
elif t >= 60:
    print ("Le temps est trop élevé, il doit maximum être en dessous de 60 minutes")
else:
    print ("Le temps est correct")


Cf = Ci * math.e ** (-(k * t)) #
print("La concentration finale de l'expérience est : ",Cf)





import math
Ci = float(input("Entrer la concentration intiale (mg/L) : ")) #concentration intitiale en mg/L
if Ci <= 0.5:
    print("La concentration initiale n'est pas assez élevée")
elif Ci >= 10:
    print ("La concentration initiale est trop élevée")
else:
    print("La concentration initiale est correcte")

k = float(input("Entrer la constante empirique (L/(mg*min)) : ")) #constante empirique
if k <= 0.1:
    print("La constante empirique n'est pas assez élevée")
elif k >= 2:
    print ("La constante empirique est trop élevée")
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




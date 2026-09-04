# et si on veux que tout soit aléatoire avec certaine condition on peux refaire la meme chose mais avec quelques modifications
import math
import random

x = round(random.uniform(0.5, 10), 4)

Ci =x
x = round(random.uniform(0.5, 10), 4)
print("La concentration intiniale est de ",x," mg/L")  #concentration intitiale en mg/L

if Ci <= 0.5:
    print("La concentration initiale n'est pas assez élevée")
elif Ci >= 10:
    print ("La concentration initiale est trop élevée")
else:
    print("La concentration initiale est correcte")

y = round(random.uniform(50, 95), 4)
print( "La valeur de la constante empirique est de :",y," L/(mg*min)")
k = y #constante empirique
if k <= 50:
    print("La constante empirique n'est pas assez élevée")
elif k >= 95:
    print ("La constante empirique est trop élevée")
else:
    print("La constante empirique est correcte")

temps = round(random.uniform(1, 60), 4)
print("La valeur du temps est de :",temps," minutes")

t = (temps) #pour un temps donné aléatoirement
if t <= 0:
    print("Le temps n'est pas assez élevé, il doit minimum être au dessus de 1 minute")
elif t >= 60:
    print ("Le temps est trop élevé, il doit maximum être en dessous de 60 minutes")
else:
        print("Le temps est correct")


Cf = Ci * math.e ** (-(k * t)) 
print("La concentration finale de l'expérience est : ", Cf)
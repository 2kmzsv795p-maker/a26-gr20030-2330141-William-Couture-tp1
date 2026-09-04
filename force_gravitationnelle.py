G=6.67430e-11
def force_gravitationelle(m1, m2, r):
    return (G * m1 * m2) / (r**2)
print("La force gravitationnelle est de : ", force_gravitationelle(float(input("Entrer la masse du premier objet : ")), float(input("Entrer la masse du deuxième objet : ")), float(input("Entrer la distance entre les deux objets : "))), "N")
def energie_cinétique(masse,vitesse):
    return((masse *(vitesse**2))/2)
print("L'énergie cinétique totale est de : ", energie_cinétique(float(input("Entrer la masse de l'objet : ")), float(input("Entrer la vitesse de l'objet : "))), "J")
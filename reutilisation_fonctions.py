def aire_rectangle(longueur, largeur):
    return (longueur * largeur)
print("L'aire du  rectangle est de: ", aire_rectangle(float(input("Entrer la longueur du rectangle : ")), float(input("Entrer la largeur du rectangle : "))),"mètre carré")

def aire_prisme(longueur, largeur, hauteur):
    return (longueur * largeur * hauteur)
print("Le volume du prisme est de: ", aire_prisme(float(input("Entrer la longueur du prisme : ")), float(input("Entrer la largeur du prisme : ")), float(input("Entrer la hauteur du prisme : "))), "mètres cubes")
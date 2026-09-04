# Listes parallèles contenant les masses en g et volumes en cm3
masses_g = [135, 270, 92]
volumes_cm3 = [84, 151, 113]

# Fonction qui calcule la densité en kg/m3
def calculer_densite(masse_g, volume_cm3):
    masse_kg = masse_g / 1000
    volume_m3 = volume_cm3 / 1_000_000
    densite = masse_kg / volume_m3
    return densite

# Calcul des densités pour les 3 échantillons
densite1 = calculer_densite(masses_g[0], volumes_cm3[0])
densite2 = calculer_densite(masses_g[1], volumes_cm3[1])
densite3 = calculer_densite(masses_g[2], volumes_cm3[2])

# Affichage des résultats
print("Densité 1 :", round(densite1, 2), "kg/m3")
print("Densité 2 :", round(densite2, 2), "kg/m3")
print("Densité 3 :", round(densite3, 2), "kg/m3")
 
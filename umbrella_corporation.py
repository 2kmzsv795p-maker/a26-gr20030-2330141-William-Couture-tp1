noms         = ["Virus-T", "Virus-G", "Uroboros"]
temperatures = [37.0, 39.5, 40.0]
pH_valeurs   = [6.2, 5.8, 7.0]
mutations    = ["Stable", "Instable", "Agressive"]
specifiques  = ["Contagiosité : Élevée", "Capacité Régénérative : Extrême", "Compatibilité Hôte : Faible"]
def afficher_echantillon(nom, temperature, pH, mutation, specifique):
    print("Échantillon :", nom)
    print("Température :", temperature, "°C")
    print("pH :", pH)
    print("Mutation :", mutation)
    print(specifique)
    print("--------------------")

for i in range(len(noms)):
    afficher_echantillon(noms[i], temperatures[i], pH_valeurs[i], mutations[i], specifiques[i])

      
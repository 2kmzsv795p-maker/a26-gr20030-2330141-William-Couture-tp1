nom = ["william", "Alexis", "Charles"]
def dire_bonjour(nom):
    print("Bonjour, " + nom + "!")

for nom in nom:         #essentiel si on veux donner tout les noms de la liste
    dire_bonjour(nom)     #si on met nom[1] il va suelemnt donner la deuxième lettre du nom, si on met nom[1:3] il 
                                       # va donner la deuxieme et la troisieme lettre du nom


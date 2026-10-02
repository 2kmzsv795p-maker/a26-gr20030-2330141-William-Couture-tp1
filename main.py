from analyse import simuler_evolution, analyser_resultats


def main():
    print("=== Simulation de cinétique ===")
    c0 = float(input("Concentration initiale (mg/L) : "))
    k = float(input("Constante de dégradation (/h) : "))
    duree_heures = int(input("Durée de la simulation (heures) : "))
    seuil_min = float(input("Seuil minimal thérapeutique (mg/L) : "))
    seuil_max = float(input("Seuil toxique maximal (mg/L) : "))

    concentrations = simuler_evolution(c0, k, duree_heures)
    print(analyser_resultats(concentrations, seuil_min, seuil_max))


if __name__ == "__main__":
    main()


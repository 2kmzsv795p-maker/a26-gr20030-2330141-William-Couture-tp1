#temp= float(input("Entrer la température en Celsius : "))
def celsius_vers_fahrenheit(temp):
    return (temp * 9/5) + 32
#print("La température en Fahrenheit est de : ", celsius_vers_fahrenheit(15))
#print("La température en Fahrenheit est de : ", celsius_vers_fahrenheit(19))
#print("La température en Fahrenheit est de : ", celsius_vers_fahrenheit(20))
#print("La température en Fahrenheit est de : ", celsius_vers_fahrenheit(1))
#print("La température en Fahrenheit est de : ", celsius_vers_fahrenheit(9))

nb_fois=int(input("Combien de fois voulez-vous convertir une température en Fahrenheit ? "))

for _ in range(nb_fois):
    valeur_celsius=float(input("Entrer la température en Celsius : "))
    résultat= celsius_vers_fahrenheit(valeur_celsius)
    print(f"{valeur_celsius} °C = {résultat} °F")
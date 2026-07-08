# Fonction qui lit deux nombres
def lire_nombre():

    saisie1 = input("Entrez le premier nombre : ")
    saisie2 = input("Entrez le deuxième nombre : ")

    try:
        nombre1 = float(saisie1)
        nombre2 = float(saisie2)
        return nombre1, nombre2

    except ValueError:
        print("Erreur : veuillez entrer uniquement des nombres.")
        return None


# Fonction d'addition
def addition(nombre1, nombre2):
    return nombre1 + nombre2


# Fonction de soustraction
def soustraction(nombre1, nombre2):
    return nombre1 - nombre2


# Fonction de multiplication
def multiplication(nombre1, nombre2):
    return nombre1 * nombre2


# Fonction de division
def division(nombre1, nombre2):

    if nombre2 == 0:
        print("Erreur : division par zéro impossible.")
        return None

    return nombre1 / nombre2


# Menu principal
while True:

    print("\n==============================")
    print("       CALCULATRICE")
    print("==============================")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("0. Quitter")
    print("==============================")

    choix = input("Votre choix : ")

    # Quitter le programme
    if choix == "0":
        print("Merci d'avoir utilisé la calculatrice de Rosy.")
        break

    # Vérifier que le choix est valide
    if choix not in ["1", "2", "3", "4"]:
        print("Choix invalide.")
        continue

    # Lecture des deux nombres
    nombres = lire_nombre()

    if nombres is None:
        continue

    nombre1, nombre2 = nombres

    # Effectuer le calcul choisi
    if choix == "1":
        resultat = addition(nombre1, nombre2)
        print(f"{nombre1} + {nombre2} = {resultat}")

    elif choix == "2":
        resultat = soustraction(nombre1, nombre2)
        print(f"{nombre1} - {nombre2} = {resultat}")

    elif choix == "3":
        resultat = multiplication(nombre1, nombre2)
        print(f"{nombre1} × {nombre2} = {resultat}")

    elif choix == "4":
        resultat = division(nombre1, nombre2)

        if resultat is not None:
            print(f"{nombre1} ÷ {nombre2} = {resultat}")
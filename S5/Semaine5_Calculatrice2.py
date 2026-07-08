# Fonction qui lit les nombres saisis
 
def lire_nombres():

    saisie = input("Entrez les nombres séparés par un espace : ")

    try:
        nombres = list(map(float, saisie.split()))
        return nombres

    except ValueError:
        print("Erreur : veuillez entrer uniquement des nombres.")
        return None


# Fonction d'addition
def addition(*nombres):
    return sum(nombres)


# Fonction de soustraction
def soustraction(*nombres):

    resultat = nombres[0]

    for n in nombres[1:]:
        resultat-=n

    return resultat


# Fonction de multiplication
def multiplication(*nombres):

    resultat = 1

    for n in nombres:
        resultat *= n

    return resultat


# Fonction de division
def division(*nombres):

    resultat = nombres[0]

    for n in nombres[1:]:

        if n == 0:
            print("Erreur : division par zéro impossible.")
            return None

        resultat /= n

    return resultat


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
    print(maintenant)

    choix = input("Votre choix : ")
# Quitter le programme
    if choix == "0":
        print("Merci d'avoir utilisé la calculatrice.")
        break
 # Vérifier que le choix est valide
    if choix not in ["1", "2", "3", "4"]:
        print("Choix invalide.")
        continue
 # Lecture des deux nombres
    nombres = lire_nombres()

    if nombres is None:
        continue

    if len(nombres) == 0:
        print("Vous devez saisir au moins un nombre.")
        continue
 # Effectuer le calcul choisi
    if choix == "1":

        resultat = addition(*nombres)
        calcul = " + ".join(map(str, nombres))
        print(calcul, "=", resultat)

    elif choix == "2":

        resultat = soustraction(*nombres)
        calcul = " - ".join(map(str, nombres))
        print(calcul, "=", resultat)

    elif choix == "3":

        resultat = multiplication(*nombres)
        calcul = " × ".join(map(str, nombres))
        print(calcul, "=", resultat)

    elif choix == "4":

        resultat = division(*nombres)

        if resultat is not None:
            calcul = " ÷ ".join(map(str, nombres))
            print(calcul, "=", resultat)
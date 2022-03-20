import random

materiaux = [
    "pierre",
    "feuille",
    "ciseaux"
]

continuer = "O"

while continuer == "O":
    choixPC = random.choice(materiaux)
    print(choixPC)
    r=""
    r = input("Que voulez-vous jouer ? \nPierre (P) | Feuille (F) | Ciseaux (C) => ")
    if r == "P":
        if choixPC == "pierre":
            etat = "Egalité"
        if choixPC == "feuille":
            etat = "Gagné"
        if choixPC == "ciseaux":
            etat = "Perdu"
    if r == "F":
        if choixPC == "pierre":
            etat = "Perdu"
        if choixPC == "feuille":
            etat = "Egalité"
        if choixPC == "ciseaux":
            etat = "Gagné"
    if r == "C":
        if choixPC == "pierre":
            etat = "Gagné"
        if choixPC == "feuille":
            etat = "Perdu"
        if choixPC == "ciseaux":
            etat = "Egalité"
    print(etat + "! L'ordinateur avait choisit " + choixPC)
    continuer = input("Voulez-vous rejouer ? (O/N)")
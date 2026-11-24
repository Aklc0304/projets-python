taches = []

def sauvegarder():
    with open("taches.txt", "w", encoding="utf-8") as fichier:
        for nom in taches:
            fichier.write(nom + "\n")

def charger():
    try:
        with open("taches.txt", "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                taches.append(ligne.strip())
    except FileNotFoundError:
        pass

def ajouter_tache(nom):
    taches.append(nom)
    sauvegarder()
    print("Tache. ajoutée :", nom)

def afficher_taches():
    if len(taches) == 0:
        print("aucune tache pour le moment.")
    else:
        for numero, nom in enumerate(taches, start=1):
            print(numero, "-", nom)

def supprimer_tache(numero):
    if numero < 1 or numero > len(taches):
        print("numero invalide.")
    else:
        supprimee = taches.pop(numero - 1)
        sauvegarder()
        print("tache supprimee :", supprimee)

def vider_taches():
    if len(taches) == 0:
        print("La liste est déjà vide.")
    else:
        confirmation = input("Tout supprimer ? (o/n) : ").strip().lower()
        if confirmation == "o":
            taches.clear()
            sauvegarder()
            print("Toutes les tâches ont été supprimées.")
        else:
            print("Annulé.")        

charger()

while True:
    print()
    print("Nombre de tâches :", len(taches))
    print("1 - Ajouter une tache")
    print("2 - Afficher les taches")
    print("3 - Supprimer une tache")
    print("4 - vider toute la liste")
    print("5 - quitter")
    choix = input("Ton choix : ")

    if choix == "1":
        nom = input("Nom de la tache : ").strip()
        if nom:
            ajouter_tache(nom)
        else:
            print("impossible d'ajouter une tache vide")    
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        afficher_taches()
        try:
            numero = int(input("numero a supprimer :"))
            supprimer_tache(numero)
        except ValueError:
            print("erreur : tape un nombre, par exemle 1. ")    

    elif choix == "4":
        vider_taches()
    elif choix == "5":
        print("a bientot !")
        break    
    else:
        print("choix invalide.")                       
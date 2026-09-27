import csv
dramas = []

with open("kdrama_DATASET.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)

    for drama in lecteur:
        dramas.append(drama)
def title_search():
        search = input("Entrez le titre du K-Drama recherché : ")

        found = False

        for drama in dramas:
            if search.lower() in drama["Title"].lower():
                print("\n................................")
                print("Titre :", drama["Title"])
                print("Année :", drama["Year of release"])
                print("Note :", drama["Rating"])
                print("Genre :", drama["Genre"])
                print("Description :", drama["Description"])

                trouve = True

        if not found:
            print("Aucun K-Drama trouvé.")

def search_by_genre():
    search = input("Entrez le genre du K-Drama : ")
    found = False
    for drama in dramas:
        if search.lower() in drama["Genre"].lower():
            print("\n................................")
            print("Titre :", drama["Title"])
            print("Note :", drama["Rating"])
            print("Genre :", drama["Genre"])
            print("Description :", drama["Description"])
            found = True
    if not found:
        print("Aucun K-Drama trouvé.")

def search_by_year():
    annee = input("Entrez l'année du K-Drama : ").strip()
    found = False
    for drama in dramas:
        if annee == drama["Year of release"]:
            print("\n............ Réalisé en", drama["Year of release"],"............")
            print("Titre :", drama["Title"])
            print("Année :", drama["Rating"])
            print("Genre :", drama["Genre"])
            print("Description :", drama["Description"])
            found = True
    if not found:
        print("Aucun K-Drama trouvé.")

def search_by_note():
    note_min = float(input("Entrez la note minimum : "))
    note_max = float(input("Entrez la note maximum : "))
    found = False
    for drama in dramas:
        rating = float(drama["Rating"])
        if note_min <= rating <= note_max:
            print("\n............ Noté", drama["Rating"]," SUR 10............")
            print("Titre :", drama["Title"])
            print("Note :", drama["Year of release"])
            print("Genre :", drama["Genre"])
            print("Description :", drama["Description"])
            found = True
    if not found:
        print("Aucun K-Drama trouvé.")

def menu():
    print (" K-Drama Search ENGINE")
    print ("1 - Rechercher par titre")
    print ("2 - Rechercher par genre")
    print ("3 - Rechercher par année")
    print ("4 - Rechercher par note")

    choix = input("Choix : ").strip()
    if choix == "1":
        title_search()
    elif choix == "2":
        search_by_genre()
    elif choix == "3":
        search_by_year()
    elif choix == "4":
        search_by_note()
    else:
        print ("Choix inconnu")

menu()
print("\n")
def retry():
    print("Voulez vous recommencer ? \n")
    choix = input(" OUI ou NON ? \n").strip().lower()
    if choix == "oui":
        menu()
    elif choix == "non":
        print ("Merci d'avoir utilisé notre Search ENGINE")
    else:
        print ("Choix inconnu")

retry()
print("\n")
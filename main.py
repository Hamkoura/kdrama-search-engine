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

def menu():
    print (" K-Drama Search ENGINE")
    print ("1 - Rechercher par titre")
    print ("2 - Rechercher par genre")

    choix = input("Choix : ").strip()
    if choix == "1":
        title_search()
    elif choix == "2":
        search_by_genre()
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
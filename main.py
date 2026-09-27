import csv

def title_search():
    search = input("Entrez le titre du K-Drama recherché : ")

    with open("kdrama_DATASET.csv", "r", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)

        found = False

        for drama in lecteur:

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

title_search()
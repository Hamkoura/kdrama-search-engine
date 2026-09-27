import csv
with open("kdrama_DATASET.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)

    for drama in lecteur:
        print("...........................")
        print(drama["Title"])
        print(drama["Year of release"])
        print(drama["Rating"])
        print(drama["Genre"])
        print(drama["Description"])
        print()
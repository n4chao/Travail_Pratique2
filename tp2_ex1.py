import json
import csv

with open ("data.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

with open ("output.csv", "w", encoding="utf-8") as csv_file:
    objet_csv = csv.writer(csv_file, delimiter=',')

    for valeur in data:
        objet_csv.writerow(valeur)
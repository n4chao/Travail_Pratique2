import csv

def charger_pokémons_csv(f):
    # création d'un dictionnaire vide
    pokemons = {}

    with open("pokemon.csv", "r", encoding="utf-8") as csv_file:

        for ligne in csv_file:
            valeur = ligne.strip().split(",")

            # les nom des pokemons qui sont toujours à l'index 0 vont se faire stocker dans la liste "nom"
            global nom
            global stats

            # clé
            nom = valeur[0]
            # valeur
            stats = []

            for n in valeur[1:]:
                stats.append(int(n))

            # stocker les clés et valeurs dans le dictionnaire
            pokemons[nom] = stats

    return pokemons

# tests
pkmn = charger_pokémons_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

pkmn = charger_pokémons_csv("pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))


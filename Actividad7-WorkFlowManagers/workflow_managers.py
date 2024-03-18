import requests
from prefect import task, flow
import csv
import pandas as pd

## extract
@task
def get_complaint_data(name):
    if requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/"):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
        return r
    else:
        return 0

## transform
@task
def parse_complaint_data(raw):
    if raw == 0:
        return 0
    else:
        pokemon_info = []
        values = raw.json()
        pokemon_id = values['id']
        pokemon_name = values['name']
        pokemon_types = values['types']
        pokemon_type = pokemon_types[0]['type']['name']
        pokemon_info.append((pokemon_id, pokemon_name, pokemon_type))
        return pokemon_info 

## load
@task
def store_complaints(parsed):
    if parsed == 0:
        print("This pokemon does not exist")
    else:
        id_new_pokemon = parsed[0][0]
        if id_new_pokemon in get_pokemon_stored():
            print("This pokemon is already stored")
        else:
            with open('pokemon.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(parsed)

def get_pokemon_stored():
    df = pd.read_csv('pokemon.csv')

    num_rows = df.shape[0]
    id_stored = []
    for i in range(num_rows):
        id_stored.append(df.iloc[i]['id'])

    return id_stored


@flow
def myFlow():
    name = input("Enter a pokemon name: ")
    raw = get_complaint_data(name)
    parsed = parse_complaint_data(raw)
    store_complaints(parsed)

keep_adding = True
myFlow()
while keep_adding:
    option = input("Do you want to add another pokemon? (y/n): ")
    if option.lower() == 'y':
        myFlow()
    else:
        keep_adding = False


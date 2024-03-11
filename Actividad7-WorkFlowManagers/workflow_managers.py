import requests
from prefect import task, flow
import csv

## extract
@task
def get_complaint_data(name):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    return r

## transform
@task
def parse_complaint_data(raw):
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
    with open('pokemon.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(parsed)

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


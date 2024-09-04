import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c9b019fc7605127ab75e21e509de7c6f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}



body_create = {
    "name": "Pythonzz",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "67427",
    "name": "NewNamePython",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "67427"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text, response_create.status_code)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change )
print(response_change.text, response_change.status_code)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball )
print(response_pokeball.text, response_pokeball.status_code)

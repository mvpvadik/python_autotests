import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b281e0a01a50d39cec73db0ac3cc373f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
pokemon_id = response_create.json()['id']

body_put = {
    "pokemon_id": pokemon_id,
    "name": "Кусь",
    "photo_id": 2
}

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}
response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)






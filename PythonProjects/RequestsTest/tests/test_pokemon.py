import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b281e0a01a50d39cec73db0ac3cc373f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 4240


def test_statuscode():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_nametrainers():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Konor'


import requests

headers = {
    'Authorization': 'Bearer 376f0a25129fda22f7fc44398757efc7',
}

response = requests.post('https://shiftheroes.fr/api/v1/plannings/LQfrZg/shifts/qQFe15E/reservations', headers=headers)
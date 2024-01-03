import requests
import os

from dotenv import load_dotenv

load_dotenv()

headers = {
    'Authorization': f'Bearer {os.getenv("API_KEY")}',
}

# Récupérer la liste des plannings
response = requests.get('https://shiftheroes.fr/api/v1/plannings', headers=headers)
# Affiche la réponse JSON convertie en objet Python
print(response.json())

# Récupérer la liste des crénaux d'un planning
response = requests.get('https://shiftheroes.fr/api/v1/plannings/LQfrZg/shifts', headers=headers)
# Affiche la réponse JSON convertie en objet Python
print(response.json())

# Récupérer une réservation sur un crénau
response = requests.post('https://shiftheroes.fr/api/v1/plannings/LQfrZg/shifts/OAF6DPq/reservations', headers=headers)
# Affiche la réponse JSON convertie en objet Python
print(response.json())
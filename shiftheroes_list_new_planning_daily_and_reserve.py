import requests
import time
import os

from dotenv import load_dotenv

load_dotenv()

headers = {
    'Authorization': f'Bearer {os.getenv("API_KEY")}',
}

liste_initiale = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()

while liste_initiale == nouvelle_liste:
    nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
    print(".", end="", flush=True)
    time.sleep(1)

print("Nouveau planning disponible !")

liste_creneaux = requests.get('https://shiftheroes.fr/api/v1/plannings/'+ nouvelle_liste[0]["id"] +'/shifts', headers=headers).json()
print(liste_creneaux)

for creneau in liste_creneaux:
    requests.post('https://shiftheroes.fr/api/v1/plannings/' + nouvelle_liste[0]["id"] + '/shifts/' + creneau["id"] + '/reservations', headers=headers)
    time.sleep(0.2)

print("Réservation effectuée !")
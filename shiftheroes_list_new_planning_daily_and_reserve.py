import requests
import time

headers = {
    'Authorization': 'Bearer 376f0a25129fda22f7fc44398757efc7',
}

# Récupérer la liste des plannings

liste_initiale = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()

# On a mis un filtre pour pouvoir récupérer uniquement le planning journalier

while liste_initiale == nouvelle_liste:
    nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
    print(".", end="", flush=True)
    time.sleep(1)

print("Nouveau planning disponible !")

# L'identifiant du planning qui a changé

print(nouvelle_liste[0]["id"])

# La suite il faut récupérer la liste des crénneaux de ce nouveau planning en utilisant l'identifiant
# C'est pas évident car l'identifiant est dans une variable, à nous de savoir comment mettre une
# variable dans une chaîne de caractères (interpolation)

liste_creneaux = requests.get('https://shiftheroes.fr/api/v1/plannings/'+ nouvelle_liste[0]["id"] +'/shifts', headers=headers).json()
print(liste_creneaux)

# Maintenant il faudrait que pour chacun de ces créneaux, l'on fasse une réservation

for creneau in liste_creneaux:
    requests.post('https://shiftheroes.fr/api/v1/plannings/' + nouvelle_liste[0]["id"] + '/shifts/' + creneau["id"] + '/reservations', headers=headers)
    time.sleep(0.2)

print("Réservation effectuée !")
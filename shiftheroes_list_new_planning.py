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
    time.sleep(1)

print("Nouveau planning disponible !")

# On récupère l'identifiant du planning qui a changé

identifiant_nouveau_planning = nouvelle_liste[0]["id"]

# La suite il faut récupérer la liste des crénneaux de ce nouveau planning en utilisant l'identifiant
# C'est pas évident car l'identifiant est dans une variable, à nous de savoir comment mettre une
# variable dans une chaîne de caractères (interpolation)

liste_creneaux = requests.get('https://shiftheroes.fr/api/v1/plannings/'+ identifiant_nouveau_planning +'/shifts', headers=headers)
print(liste_creneaux.json())

# Maintenant il faudrait que pour chacun de ces créneaux, l'on fasse une réservation



for creneaux in liste_creneaux:
    identifiant_nouveau_crenaux = liste_creneaux[creneaux]["id"]
    requests.post('https://shiftheroes.fr/api/v1/plannings/LQfrZg/shifts/'+ identifiant_nouveau_crenauxneaux +'/reservations')
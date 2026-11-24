import requests

ville = input("Quelle ville ? ").strip()

if not ville:
    print("Tu n'as pas écrit de ville.")
    exit()

try:
    url_geo = "https://geocoding-api.open-meteo.com/v1/search"
    reponse_geo = requests.get(
        url_geo,
        params={"name": ville, "count": 1, "language": "fr"},
        timeout=10,
    )
    donnees_geo = reponse_geo.json()

    resultats = donnees_geo.get("results")
    if not resultats:
        print("Ville introuvable :", ville)
        exit()

    lieu = resultats[0]

    url_meteo = "https://api.open-meteo.com/v1/forecast"
    reponse_meteo = requests.get(
        url_meteo,
        params={
            "latitude": lieu["latitude"],
            "longitude": lieu["longitude"],
            "current_weather": "true",
        },
        timeout=10,
    )
    meteo = reponse_meteo.json()["current_weather"]

except requests.exceptions.RequestException:
    print("Erreur : impossible de contacter le service météo. Vérifie ta connexion Internet.")
    exit()

print("Météo actuelle à", lieu["name"], "(" + lieu["country"] + ")")
print("Température :", meteo["temperature"], "°C")
print("Vent :", meteo["windspeed"], "km/h")
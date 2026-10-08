import requests 
url = "https://api.open-meteo.com/v1/forecast", 
params={"latitude": 45.46, "longitude": -73.47,
 "current": "temperature_2m"},
try: 
    r = requests.get(url,params=params,timeout=10) 
    r.raise_for_status() 
    donnees = r.json() 
except  requests.RequestException as erreur:
    print(f"API indisponible : {erreur}") 
except ValueError:
    print("Réponse JSON invalide")
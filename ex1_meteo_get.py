import requests 
reponse = requests.get( 
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 45.46, "longitude": -73.47, 
    "current": "temperature_2m"}, 
     headers={"Accept": "application/json"},
     timeout=10,
     )
reponse.raise_for_status() 
donnees = reponse.json() 
actuel = donnees.get("current", {}) 
temperature = actuel.get("temperature_2m")
print(f"{temperature} °C")
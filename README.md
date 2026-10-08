import requests 
reponse = requests.get( 
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 45.46, "longitude": -73.47, 
    "current": "temperature_2m"}, 
     headers={"Accept": "application/json"},
      )
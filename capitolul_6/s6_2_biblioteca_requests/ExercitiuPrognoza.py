import requests

#Pe baza documentației vom face o căutare după numele orașului și vom extrage valoarea de woeidw
url_baza = 'https://www.metaweather.com/api/location/search/?query=bucharest'

#Extragem JSON-ul din rezultat
rasp = requests.get(url_baza).json()

#Deoarece am făcut o căutare cu URL-ul de mai sus, rezultatul este constituit dintr-o listă
#Vom avea un singur rezultat în 0, deci putem prelua direct elementul cu index 0 și să extragem woeid-ul
woeid_buc = rasp[0]['woeid']

#Construim URL-ul pentru extragerea informațiilor meteo
url_vreme = f'https://www.metaweather.com/api/location/{woeid_buc}'
rasp = requests.get(url_vreme).json()

info_meteo = rasp['consolidated_weather']
#În cadrul info_meteo vom avea o listă ce conține prognoza pentru ziua curentă și următoarele zile
#Întrucât ne interesează doar ziua curentă, vom extrage doar elementul de pe prima poziție
info_meteo = info_meteo[0]

print(f"Data pentru prognoza: {info_meteo['applicable_date']}")
print(f"Temperatura maxima: {info_meteo['min_temp']}C")
print(f"Temperatura maxima: {info_meteo['max_temp']}C")
print(f"Umiditate: {info_meteo['humidity']}%")

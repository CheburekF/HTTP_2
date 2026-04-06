import sys
import requests
from PIL import Image
from io import BytesIO
from map_params import get_map_params

GEOCODER_URL = "http://geocode-maps.yandex.ru/1.x/"
GEOCODER_KEY = "8013b162-6b42-4997-9691-77b7074026e0"
STATIC_URL = "https://static-maps.yandex.ru/v1"
STATIC_KEY = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

toponym_to_find = " ".join(sys.argv[1:])

geocoder_params = {
    "apikey": GEOCODER_KEY,
    "geocode": toponym_to_find,
    "format": "json",
}

response = requests.get(GEOCODER_URL, params=geocoder_params)
if not response:
    print("Ошибка геокодера:", response.status_code, response.reason)
    sys.exit(1)

json_response = response.json()
members = json_response["response"]["GeoObjectCollection"]["featureMember"]
if not members:
    print("Объект не найден.")
    sys.exit(1)

toponym = members[0]["GeoObject"]
map_params = get_map_params(toponym, STATIC_KEY)

response = requests.get(STATIC_URL, params=map_params)
if not response:
    print("Ошибка StaticAPI:", response.status_code, response.reason)
    sys.exit(1)

image = Image.open(BytesIO(response.content))
image.show()

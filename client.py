import requests
#import json

body = {
    "CarCount": 57,
    "BikeCount": 6,
    "BusCount": 15,
    "TruckCount": 16
}

response = requests.post(url='http://127.0.0.1:8000/predict', json=body)

print(response.json())
#try:
#    response_data = response.json()
#    print(response_data)
#except json.JSONDecodeError as e:
#    print(f"Error al decodificar la respuesta JSON: {e}")
#except Exception as e:
#    print(f"Error en la solicitud: {e}")

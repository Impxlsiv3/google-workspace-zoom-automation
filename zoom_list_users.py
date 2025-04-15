import requests

JWT_TOKEN = 'your_jwt_token'

headers = {
    'authorization': f'Bearer {JWT_TOKEN}',
    'content-type': 'application/json'
}

response = requests.get("https://api.zoom.us/v2/users", headers=headers)
print(response.json())

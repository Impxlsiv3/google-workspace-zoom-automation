import requests

API_KEY = 'your_zoom_api_key'
API_SECRET = 'your_zoom_api_secret'
JWT_TOKEN = 'your_jwt_token'

headers = {
    'authorization': f'Bearer {JWT_TOKEN}',
    'content-type': 'application/json'
}

payload = {
    "topic": "Team Sync",
    "type": 2,
    "start_time": "2025-04-20T10:00:00",
    "duration": "30",
    "timezone": "America/New_York",
    "settings": {"host_video": True, "participant_video": True}
}

response = requests.post("https://api.zoom.us/v2/users/me/meetings", json=payload, headers=headers)
print(response.json())

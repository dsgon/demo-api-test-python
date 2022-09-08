import requests

URL = 'https://petstore.swagger.io/v2/pet'

payload = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.post(url=URL,json=payload)
response_json = response.json()
print(response_json['name'])

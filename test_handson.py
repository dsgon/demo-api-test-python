import requests

URL = 'https://petstore.swagger.io/v2/pet'

def test_post_pet():
    # Config
    name = 'HandsOn'
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": name,
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
    #Pasos
    response = requests.post(url=URL,json=payload)

    #Verificaciones
    assert 200 == response.status_code , 'Status Code Invalido'
    assert name == response.json()['name']

def test_get_by_status():
        status = 'available'
        url_status = f'{URL}/findByStatus?status={status}'
        response = requests.get(url=url_status)
        assert 200 == response.status_code , 'Status Code Invalido'
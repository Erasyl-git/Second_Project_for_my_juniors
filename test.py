import requests

url = "http://127.0.0.1:8000/api/tasks/task/"

data = {
    "project": 1,
    "title": "Сделать API",
    "details": "Создать backend с помощью DRF",
    "priority": 5,
    "status": "новая"
}

response = requests.post(url, json=data)

print(response.json())
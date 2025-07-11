import requests

url = "http://127.0.0.1:8000/api/projects/project/2/"

data = {
    "title": "Портфолио, (обнова)",
    "description": "Мой личный сайт с проектами (обнова)",
    "is_active": False
}

response = requests.put(url, json=data)

print(response.json())
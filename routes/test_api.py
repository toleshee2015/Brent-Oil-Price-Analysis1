import requests

response = requests.get("http://127.0.0.1:5000/api/prices")

print(response.status_code)
print(response.json())
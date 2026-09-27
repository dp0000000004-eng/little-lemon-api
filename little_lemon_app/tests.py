from django.test import TestCase

# Create your tests here.

import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkwNDM1NjExLCJpYXQiOjE3OTA0MzUzMTEsImp0aSI6ImNlOGFiMjlkM2Y3ZDQ1YmI5NzFkMWIwOWU5Y2M0MTNhIiwidXNlcl9pZCI6IjEifQ.njfHCFiYK_ZjlJdDrgYkojMofQSmwbXXObgtTgZgOBk"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept":"application/json"
}

response = requests.get(
    "http://127.0.0.1:8000/api/data/",
    headers=headers
)

print(response.json())
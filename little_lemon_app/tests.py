from django.test import TestCase

# Create your tests here.

import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkwNTAwNTU1LCJpYXQiOjE3OTA1MDAyNTUsImp0aSI6ImU1M2EyOTJlYzU5MzQ1NGE4MmVlYzFlNjFhZWE3OTc5IiwidXNlcl9pZCI6IjEifQ.LX-3Q6R2cev5aHMpLl73BX-Asu1c9nRFOdTHZeyC-IM"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept":"application/json"
}

response = requests.get(
    "http://127.0.0.1:8000/api/data/",
    headers=headers
)

print(response.json())
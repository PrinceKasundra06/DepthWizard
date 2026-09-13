import requests

try:
    response = requests.post(
        "http://localhost:8000/api/process",
        files={"file": open("website/backend/uploads/045984f5-acf1-40b8-8780-cf8dabb1dd92.jpg", "rb")}
    )
    print(response.status_code)
    print(response.json())
except Exception as e:
    print(e)

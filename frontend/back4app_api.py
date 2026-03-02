import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("BACK4APP_APP_ID")
API_KEY = os.getenv("BACK4APP_API_KEY")

BASE_URL = "https://parseapi.back4app.com/classes/Student"

HEADERS = {
    "X-Parse-Application-Id": APP_ID,
    "X-Parse-REST-API-Key": API_KEY,
    "Content-Type": "application/json",
}

def add_student(name, age, course):
    data = {
        "name": name,
        "age": age,
        "course": course,
    }

    requests.post(BASE_URL, json=data, headers=HEADERS)


def get_students():
    response = requests.get(BASE_URL, headers=HEADERS)
    return response.json()["results"]

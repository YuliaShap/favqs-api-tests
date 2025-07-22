import random
import string

import requests
from config import BASE_URL, HEADERS


def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def create_user():
    login = f"user_{random_string()}"
    email = f"{login}@example.com"
    password = "Qwerty123!"

    user_data = {
        "user": {
            "login": login,
            "email": email,
            "password": password
        }
    }
    url = f"{BASE_URL}/users"
    response = requests.post(url, json=user_data, headers=HEADERS)
    if not response.ok:
        raise Exception(f"Failed to create user: {response.status_code} - {response.text}")
    data = response.json()
    user_token = data.get("User-Token")
    if not user_token:
        raise Exception("No User-Token found in response")

    return user_token, login, email


def get_user(login, user_token):
    url = f"{BASE_URL}/users/{login}"
    headers = HEADERS.copy()
    headers["User-Token"] = user_token
    response = requests.get(url, headers=headers)
    if not response.ok:
        raise Exception(f"Failed to get user: {response.status_code} - {response.text}")

    return response.json()


def update_user(login, user_token, new_login, new_email):
    url = f"{BASE_URL}/users/{login}"
    headers = HEADERS.copy()
    headers["User-Token"] = user_token

    user_data = {
        "user": {
            "login": new_login,
            "email": new_email
        }
    }
    response = requests.put(url, json=user_data, headers=headers)
    if not response.ok:
        raise Exception(f"Failed to update user: {response.status_code} - {response.text}")

    return response.json()

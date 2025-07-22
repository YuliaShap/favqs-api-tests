import requests
from config import BASE_URL, HEADERS


def create_user():
    """Create a new user and return the user token and login."""
    url = f"{BASE_URL}/users"
    user_data = {
        "user": {
            "login": "user_login_here",
            "email": "user_email_here",
            "password": "user_password_here"
        }
    }
    response = requests.post(url, json=user_data, headers=HEADERS)
    if not response.ok:
        raise Exception(f"Failed to create user: {response.status_code} - {response.text}")

    data = response.json()
    user_token = data["User-Token"]
    login = data["login"]
    return user_token, login


def get_user(login, user_token):
    """Retrieve user details by login."""
    url = f"{BASE_URL}/users/{login}"
    headers = HEADERS.copy()
    headers["User-Token"] = user_token
    response = requests.get(url, headers=headers)
    if not response.ok:
        raise Exception(f"Failed to get user: {response.status_code} - {response.text}")
    return response.json()


def update_user(login, user_token, new_login, new_email):
    """Update user login and email."""
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

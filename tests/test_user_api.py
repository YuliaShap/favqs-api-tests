from api.user_api import create_user, get_user, update_user, random_string


def test_create_and_get_user():
    user_token, login, email = create_user()
    user_data = get_user(login, user_token)
    assert user_data["login"] == login
    assert user_data["account_details"]["email"] == email


def test_update_user():
    user_token, login, email = create_user()
    new_login = f"new_{random_string()}"
    new_email = f"{new_login}@example.com"
    update_user(login, user_token, new_login, new_email)
    user_data = get_user(new_login, user_token)
    assert user_data["login"] == new_login
    assert user_data["account_details"]["email"] == new_email




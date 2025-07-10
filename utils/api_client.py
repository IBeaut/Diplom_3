import requests

class ApiClient:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    @staticmethod
    def create_user(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f"{ApiClient.BASE_URL}/auth/register", json=payload)
        if response.status_code != 200:
            raise Exception(f"Failed to create user: {response.status_code} - {response.text}")
        return response

    @staticmethod
    def delete_user(token):
        headers = {"Authorization": token}
        response = requests.delete(f"{ApiClient.BASE_URL}/auth/user", headers=headers)
        if response.status_code != 202:
            print(f"Warning: Failed to delete user: {response.status_code} - {response.text}")
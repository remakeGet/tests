import pytest
import requests
from requests.auth import HTTPBasicAuth

class TestYandexDiskAPI:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
    TOKEN = "your_yandex_token"  # Замените на реальный токен
    
    @pytest.mark.parametrize("folder_name,expected_code", [
        ("test_folder", 201),  # Успешное создание
        ("test_folder", 409),  # Папка уже существует
        ("", 400)             # Неверный запрос
    ])
    def test_create_folder(self, folder_name, expected_code):
        headers = {"Authorization": f"OAuth {self.TOKEN}"}
        params = {"path": f"/{folder_name}"}
        
        response = requests.put(self.BASE_URL, headers=headers, params=params)
        assert response.status_code == expected_code
        
        # Для успешного создания проверяем наличие папки
        if expected_code == 201:
            check_response = requests.get(
                self.BASE_URL,
                headers=headers,
                params={"path": "/"}
            )
            assert folder_name in [item["name"] for item in check_response.json()["_embedded"]["items"]]
    
    def test_create_folder_unauthorized(self):
        response = requests.put(
            self.BASE_URL,
            params={"path": "/unauthorized_test"}
        )
        assert response.status_code == 401

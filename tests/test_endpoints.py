import pytest
import requests


BASE_URL = "http://localhost:8080"

# Valid endpoints
@pytest.mark.parametrize("endpoint", [
    ("/about"),
    ("/browser-check"),
    ("/settings"),
    ("/server.log"),
])
def test_valid_endpoints(endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}")
    assert response.status_code == 200

# Invalid endpoints
@pytest.mark.parametrize("endpoint", [
    ("/about.html"),
    ("/browser-check.html"),
    ("/intro.html"),
    ("/settings.html"),
    ("/tutor.html"),
])
def test_invalid_endpoints(endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}")
    assert response.status_code == 404

import pytest
import requests

BASE_URL = "http://localhost:3000"

@pytest.mark.parametrize("endpoint, expected_status", [
    ("/users", 200),
    ("/products", 200),
    ("/invalid-route", 404),
])
def test_endpoints(endpoint, expected_status):
    response = requests.get(f"{BASE_URL}{endpoint}")
    assert response.status_code == expected_status

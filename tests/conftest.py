import pytest
import requests

BASE_URL = "http://localhost:8080"

def is_site_running():
    try:
        response = requests.get(BASE_URL, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

@pytest.hookimpl(tryfirst=True)
def pytest_runtestloop(session):
    if not is_site_running():
        pytest.exit("Aborting: The site is down.")


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI - Sonar Test Project"}

def test_add_numbers():
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.json()["result"] == 5

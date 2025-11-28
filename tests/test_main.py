from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_add_numbers():
    response = client.get("/add/3/4")
    assert response.status_code == 200
    assert response.json() == {"result": 7}

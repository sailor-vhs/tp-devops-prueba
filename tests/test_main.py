from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_list_items():
    r = client.get("/items")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_create_item():
    r = client.post("/items", json={"name": "Item C"})
    assert r.status_code == 200
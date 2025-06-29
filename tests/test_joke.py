
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_joke_replaces_name(monkeypatch):
    def fake_fetch():
        return "Meow Norris can break the internet."

    monkeypatch.setattr("app.api.joke.fetch_joke", fake_fetch)
    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json() == {"joke": "Meow Norris can break the internet."}


from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_joke_replaces_chuck_norris(monkeypatch):
    async def fake_get_joke():
        return "Meow Norris can break the internet."

    # Mock the function where it's imported and used in the endpoint
    monkeypatch.setattr("app.api.joke.fetch_chuck_norris_joke", fake_get_joke)

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json() == {"joke": "Meow Norris can break the internet."}

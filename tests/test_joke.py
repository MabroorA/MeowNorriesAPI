
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_joke_replaces_chuck_norris(monkeypatch):
    async def fake_get_joke():
        return {"value": "Chuck Norris can break the internet."}

    monkeypatch.setattr("app.api.joke.fetch_chuck_norris_joke", fake_get_joke)

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json() == {"joke": "Meow Norris can break the internet."}


def test_joke_api_returns_503_on_fetch_failure(monkeypatch):
    async def fake_get_joke():
        raise Exception("External API error")

    monkeypatch.setattr("app.api.joke.fetch_chuck_norris_joke", fake_get_joke)

    response = client.get("/joke")
    assert response.status_code == 503
    assert response.json() == {"detail": "Failed to fetch joke from external API"}


def test_joke_with_multiple_chuck_norris(monkeypatch):
    async def mock_fetch():
        return {"value": "Chuck Norris fought Chuck Norris and lost."}

    monkeypatch.setattr("app.api.joke.fetch_chuck_norris_joke", mock_fetch)

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json()["joke"] == "Meow Norris fought Meow Norris and lost."

def test_joke_without_chuck_norris(monkeypatch):
    async def mock_fetch():
        return {"value": "The internet is down."}

    monkeypatch.setattr("app.api.joke.fetch_chuck_norris_joke", mock_fetch)

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json() == {"joke": "The internet is down."}

def test_joke_with_lowercase_chuck_norris(monkeypatch):
    async def mock_fetch():
        return {"value": "Did you know chuck norris can divide by zero?"}

    monkeypatch.setattr("app.api.joke.fetch_chuck_norris_joke", mock_fetch)

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json()["joke"] == "Did you know Meow Norris can divide by zero?"

def test_joke_api_response_missing_value_key(monkeypatch):
    async def mock_fetch_missing_value():
        return {}

    monkeypatch.setattr("app.api.joke.fetch_chuck_norris_joke", mock_fetch_missing_value)

    response = client.get("/joke")
    assert response.status_code == 503
    assert response.json() == {"detail": "Failed to fetch joke from external API"}




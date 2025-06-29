from fastapi.testclient import TestClient
from app.main import app
from app.services.joke_service import JokeServiceError

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Are you ready to be entertained?"}


def test_joke_replaces_chuck_norris(monkeypatch):
    async def mock_fetch_chuck_norris_joke():
        return {"value": "Chuck Norris can break the internet."}

    monkeypatch.setattr("app.services.joke_service.fetch_chuck_norris_joke", mock_fetch_chuck_norris_joke)

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json() == {"joke": "Meow Norris can break the internet."}


def test_joke_api_returns_503_on_fetch_failure(monkeypatch):
    async def mock_fetch_with_exception():
        raise JokeServiceError("External API error")

    monkeypatch.setattr("app.services.joke_service.fetch_chuck_norris_joke", mock_fetch_with_exception)

    response = client.get("/joke")
    assert response.status_code == 503
    assert response.json() == {"detail": "Failed to fetch joke from external API"}


def test_joke_with_multiple_chuck_norris(monkeypatch):
    async def mock_fetch_multiple_chuck_norris():
        return {"value": "Chuck Norris fought Chuck Norris and lost."}

    monkeypatch.setattr("app.services.joke_service.fetch_chuck_norris_joke", mock_fetch_multiple_chuck_norris)

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json()["joke"] == "Meow Norris fought Meow Norris and lost."

def test_joke_without_chuck_norris(monkeypatch):
    async def mock_fetch_non_chuck_joke():
        return {"value": "The internet is down."}

    monkeypatch.setattr("app.services.joke_service.fetch_chuck_norris_joke", mock_fetch_non_chuck_joke)

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json() == {"joke": "The internet is down."}

def test_joke_with_lowercase_chuck_norris(monkeypatch):
    async def mock_fetch_lowercase_chuck_joke():
        return {"value": "Did you know chuck norris can divide by zero?"}

    monkeypatch.setattr("app.services.joke_service.fetch_chuck_norris_joke", mock_fetch_lowercase_chuck_joke)

    response = client.get("/joke")
    assert response.status_code == 200
    assert response.json()["joke"] == "Did you know Meow Norris can divide by zero?"

def test_joke_api_response_missing_value_key(monkeypatch):
    async def mock_fetch_missing_value():
        return {}

    monkeypatch.setattr("app.services.joke_service.fetch_chuck_norris_joke", mock_fetch_missing_value)

    response = client.get("/joke")
    assert response.status_code == 503
    assert response.json() == {"detail": "Failed to fetch joke from external API"}




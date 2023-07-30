import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_valid_request():
    data = {"text": "This is a valid request."}
    response = client.post("/embed", json=data)
    assert response.status_code == 200
    assert response.json() is not None

def test_invalid_field():
    data = {"invalid_field": "This is an invalid request."}
    response = client.post("/embed", json=data)
    assert response.status_code == 422
    assert "detail" in response.json()

@pytest.mark.parametrize("text", ["", " ", "\t", "\n"])
def test_empty_text_request(text):
    data = {"text": text}
    response = client.post("/embed", json=data)
    assert response.status_code == 422
    assert "detail" in response.json()

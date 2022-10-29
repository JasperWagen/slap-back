from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_lipsum_sentence_200():

    response = client.get("/lipsum/")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], str)


def test_lipsum_words_200():

    response = client.get("/lipsum?words=10")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], str)
    assert response.json()["message"].count(" ") == 9


def test_lipsum_words_422_wrong_type():

    response = client.get("/lipsum?words=test")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "type_error.integer"


def test_lipsum_words_422_negative_int():

    response = client.get("/lipsum?words=-4")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "value_error.number.not_ge"


def test_lipsum_words_422_too_large():

    response = client.get("/lipsum?words=1001")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "value_error.number.not_le"


def test_lipsum_lines_200():

    response = client.get("/lipsum?lines=10")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], str)


def test_lipsum_lines_422_wrong_type():

    response = client.get("/lipsum?lines=test")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "type_error.integer"


def test_lipsum_lines_422_negative_int():

    response = client.get("/lipsum?lines=-4")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "value_error.number.not_ge"


def test_lipsum_lines_422_too_large():

    response = client.get("/lipsum?lines=1001")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "value_error.number.not_le"

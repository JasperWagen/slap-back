def test_lipsum_sentence_200(client):

    response = client.post("/echo/", json={"message": "test"})
    assert response.status_code == 200
    assert response.json()["message"] == "test"


def test_lipsum_sentence_200(client):

    response = client.post("/echo/", json={"message": "test"})
    assert response.status_code == 200
    assert response.json()["message"] == "test"

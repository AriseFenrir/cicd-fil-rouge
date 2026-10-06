def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 500
    assert response.json()["status"] == "ok"

def test_server_root_page(client):
    response = client.get(
        '/'
    )

    assert response.status_code == 200
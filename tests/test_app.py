import app


def test_home():
    response = app.app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b"Majhe Naav Sahil Sawant"

import app


def test_home():
    assert app.app.test_client().get('/').data == b'Majhe Naav Sahil Sawant'

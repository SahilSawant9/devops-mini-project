# tests/test_app.py

import app
import sys
import os

# Ensure Python can find app.py during test
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_home():
    response = app.app.test_client().get('/')
    assert response.data == b'Majhe Naav Sahil Sawant'

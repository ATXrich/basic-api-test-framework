"""
This module is used to define fixtures that are used in the tests.
"""

import pytest
import requests


@pytest.fixture(scope='session')
def admin_login():
    payload = {'username': 'admin', 'password': 'admin'}
    response = requests.post('http://localhost:8080/auth/login', data=payload, timeout=10)
    assert response.ok
    
    access_token = response.json()['access_token']
    yield access_token


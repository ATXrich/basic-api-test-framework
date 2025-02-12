"""
This module is used to define fixtures that are used in the tests.
"""

import sys, os
import pytest
import requests

from config import SESSION, APP_URL, ADMIN_LOGIN_CREDS


# Returns access token for admin user
@pytest.fixture(scope='session')
def admin_login():
    payload = ADMIN_LOGIN_CREDS
    response = SESSION.post(f'{APP_URL}/auth/login', data=payload, timeout=10)
    assert response.ok
    
    access_token = response.json()['access_token']
    yield access_token

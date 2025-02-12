"""
This module is used to define fixtures that are used in the tests.
"""

import sys, os
import pytest
import requests
import logging

from config import SESSION, APP_URL, ADMIN_USER, ADMIN_PASSWORD, LOG


# Returns access token for admin user
@pytest.fixture(scope='session')
def admin_login():
    LOG.info('admin_login()')
    payload = {'username': ADMIN_USER, 'password': ADMIN_PASSWORD}
    LOG.debug(f'Login payload: {payload}')
    response = SESSION.post(f'{APP_URL}/auth/login', data=payload, timeout=10)
    assert response.ok
    
    access_token = response.json()['access_token']
    yield access_token

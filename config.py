"""
Constant values to be used across all tests
"""

import requests

SESSION = requests.Session()
APP_URL = 'http://localhost:8080'
ADMIN_LOGIN_CREDS = {'username': 'admin', 'password': 'admin'}

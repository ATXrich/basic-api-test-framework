import pytest
import requests

from lib.utils import build_request_headers
from lib.comments import Comments

from config import APP_URL

def test_get_all_comments(admin_login):
    
    response = Comments().get_all_comments(APP_URL, admin_login)
    assert response.ok


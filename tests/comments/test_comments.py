import pytest
import requests

import logging
from lib.utils import build_request_headers
from lib.comments import Comments


from config import APP_URL, LOG

def test_get_all_comments(admin_login):
    LOG.info('test_get_all_comments()')
    response = Comments().get_all_comments(APP_URL, admin_login)
    LOG.debug(response.json())
    assert response.ok


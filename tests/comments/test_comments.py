import pytest
import requests

import logging
from lib.utils import build_request_headers
from lib.comments import Comments

from config import APP_URL, LOG

def test_get_all_comments(admin_login):
    response = Comments().get_all_comments(APP_URL, admin_login)
    LOG.debug(response.json())
    assert response.ok

def test_create_update_delete_comment(admin_login):
    LOG.info('test_create_update_delete_comment()')

    # Create a comment
    comment = 'My first post'
    response = Comments().create_comment(APP_URL, admin_login, comment)
    assert response.ok
    response_body = response.json()
    comment_id = response_body['id']
    LOG.debug(response.json())
    assert response_body['comment_text'] == comment
    
    # Update the comment
    update_comment = f'New post on id {comment_id}'
    response = Comments().update_comment(APP_URL, admin_login, comment_id, comment=update_comment, likes=1)
    assert response.ok
    response_body = response.json()
    LOG.debug(response.json())
    assert response_body['comment_text'] ==  update_comment
    assert response_body['likes'] == 1

    # Delete the comment
    response = Comments().delete_comment(APP_URL, admin_login, comment_id)
    assert response.ok
    response_body = response.json()
    LOG.debug(response.json())
    assert response_body['detail'] == f'Deleted comment {comment_id}'
    


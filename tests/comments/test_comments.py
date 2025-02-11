import pytest
import requests


def test_get_all_comments(admin_login):
    
    request_header = {
        'Authorization': f'Bearer {admin_login}',
        'Accept': 'application/json'
    }

    response = requests.get('http://localhost:8080/comments', headers=request_header, timeout=10)
    assert response.ok


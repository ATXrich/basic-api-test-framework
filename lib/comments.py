import requests

from lib.utils import build_request_headers
from config import SESSION, LOG


class Comments:

    def __init__(self):
        self.comment_url = '/comments'

    def get_all_comments(self, app_url, access_token):
        LOG.info('get_all_comments()')
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f'{app_url}{self.comment_url}', headers=request_headers, timeout=10)
        return response

    def create_comment(self, app_url, access_token, comment):
        LOG.info('create_comment()')
        request_headers = build_request_headers(access_token)
        payload = {'text': comment}
        LOG.debug(f'Payload: {payload}')
        response = SESSION.post(f'{app_url}{self.comment_url}', headers=request_headers, params=payload, timeout=10)
        return response
    
    def update_comment(self, app_url, access_token, comment_id, **kwargs):
        LOG.info('update_comment()')
        request_headers = build_request_headers(access_token, content_type='application/json')
        payload = {}

        if 'comment' in kwargs:
            payload['comment_text'] = kwargs['comment']
        if 'likes' in kwargs:
            payload['likes'] = kwargs['likes']
        
        LOG.debug(f'Request payload: {payload}')
        response = SESSION.put(f'{app_url}{self.comment_url}/{comment_id}', headers=request_headers, json=payload, timeout=10)
        return response
    
    def delete_comment(self, app_url, access_token, comment_id):
        LOG.info('delete_comment()')
        request_headers = build_request_headers(access_token)
        response = SESSION.delete(f'{app_url}{self.comment_url}/{comment_id}', headers=request_headers, timeout=10)
        return response

    
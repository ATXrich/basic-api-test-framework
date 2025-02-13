"""
contains utility functions
"""

from config import LOG
from config import HideSensitiveInfoFilter

# returns request headers for API requests
def build_request_headers(access_token, accept_type='application/json', **kwargs):
    LOG.info('build_request_headers()')
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': accept_type
    }
    if 'content_type' in kwargs:
        headers['Content-Type'] = kwargs['content_type']

    LOG.debug(f'Headers: {headers}')

    return headers

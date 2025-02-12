"""
contains utility functions
"""

# returns request headers for API requests
def build_request_headers(access_token, content_type='application/json'):
    return {
        'Authorization': f'Bearer {access_token}',
        'Accept': content_type
    }

"""
Constant values to be used across all tests
"""

import requests
import logging
import re
import os


SESSION = requests.Session()
LOG = logging.getLogger()

APP_URL = os.getenv('APP_URL', '')
ADMIN_USER = os.getenv('ADMIN_USER', '')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', '')

class HideSensitiveInfoFilter(logging.Filter):
    def filter(self, record):
        record.msg = str(record.msg).replace(ADMIN_PASSWORD, '********')
        record.msg = re.sub(r'Authorization.*?,','Authorization\': \'******\', ', str(record.msg))
        
        return True
    
LOG.addFilter(HideSensitiveInfoFilter())

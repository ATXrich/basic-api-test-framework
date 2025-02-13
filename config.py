"""
Constant values to be used across all tests
"""

import requests
import logging
import re


SESSION = requests.Session()
APP_URL = 'http://host.docker.internal:8080'
ADMIN_USER = 'admin'
ADMIN_PASSWORD = 'admin'

LOG = logging.getLogger()

class HideSensitiveInfoFilter(logging.Filter):
    def filter(self, record):
        record.msg = str(record.msg).replace(ADMIN_PASSWORD, '********')
        record.msg = re.sub(r'Authorization.*?,','Authorization\': \'******\', ', str(record.msg))
        
        return True
    
LOG.addFilter(HideSensitiveInfoFilter())

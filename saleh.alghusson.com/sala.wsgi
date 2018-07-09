#!/usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0 , "/var/www/sala/saleh.alghusson.com")

from sala import app as application
application.secret_key = "oYxqOsdt9lEs7jp4t6VqeVCwzzHXMnqtQkLU3ZJsm6kNxRDrdOEHFDFaDwU5K4h5tUYEKuWof757oN42"

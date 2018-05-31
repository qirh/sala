#!/usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0 , "/var/www/sala/saleh.alghusson.com")

from sala import app as application
application.secret_key = "6qiT8lqCDLUiLygFFfU0EgME8o43bhgaIaJ7JgjG"

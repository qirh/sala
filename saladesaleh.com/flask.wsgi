#!/usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0 , "/var/www/sala/saladesaleh.com")

from sala import app as application
application.secret_key = "VivirSinElMar"

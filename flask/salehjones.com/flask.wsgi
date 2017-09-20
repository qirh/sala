#!/usr/bin/python
import sys
import logging
logging.basicConfig( stream = sys . stderr )
sys.path.insert ( 0 , "/var/www/flask/salehjones.com" )
from downing import app as application
application.secret_key = 'vivirsinelmar'

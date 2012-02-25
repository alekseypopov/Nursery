import os
import sys

path = '/srv/nursery/Nursery'
if path not in sys.path:
	sys.path.insert(0, '/srv/nursery/Nursery')

os.environ['DJANGO_SETTINGS_MODULE'] = 'nursery.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


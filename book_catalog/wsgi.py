# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 4

"""
WSGI config for book_catalog project.
Same as ASGI, kept it simple.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_catalog.settings')

application = get_wsgi_application()

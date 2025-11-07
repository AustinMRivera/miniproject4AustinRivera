# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 4

"""
ASGI config for book_catalog project.
I didn't change much here since it's mostly boilerplate.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_catalog.settings')

application = get_asgi_application()

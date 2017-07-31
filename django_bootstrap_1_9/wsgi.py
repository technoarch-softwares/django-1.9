"""
WSGI config for django_bootstrap_1_9 project. #Name_change

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_bootstrap_1_9.settings") #Name_change

application = get_wsgi_application()
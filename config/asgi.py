"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
>>>>>>> 3d4f397a324450a04a362f7d9feb23d25a1b81ea
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()

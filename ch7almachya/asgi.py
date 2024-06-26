import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import user.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ch7almachya.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            user.routing.websocket_urlpatterns
        )
    )
})


import os

from channels.routing import ProtocolTypeRouter,  URLRouter
from django.core.asgi import get_asgi_application
from app import routing
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'layer.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket" :  AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
})
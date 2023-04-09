import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import runtime.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'playhere.settings')

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : URLRouter(
        runtime.routing.websocket_urlpatterns
    )
})

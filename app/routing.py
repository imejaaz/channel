from django.urls import path
from . import consumer



websocket_urlpatterns=[

path('ws/sc/', consumer.sconsumer.as_asgi()),
path('ws/asc/', consumer.asconsumer.as_asgi())
]
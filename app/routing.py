from django.urls import path
from . import consumer



websocket_urlpatterns=[

path('ws/sc/<str:GroupName>/', consumer.sconsumer.as_asgi()),
path('ws/asc/<str:GroupName>/', consumer.asconsumer.as_asgi())
]
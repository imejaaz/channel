from channels.consumer import AsyncConsumer
from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
import json



class sconsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })
        print('connected')
        async_to_sync(self.channel_layer.group_add)(
            'programmers',
            self.channel_name
        )
        print('channel name......',self.channel_name)
    def websocket_receive(self, event):

        message = event['text']
        print(message)
        async_to_sync(self.channel_layer.group_send)(    
        'programmers',
        {
            'type':'chat.message',
            'message':event['text']
        })
    def chat_message(self, event):
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })
    def websocket_disconnect(self, event):
        print("connection disconnected...", event)
        print('channel layer is...', self.channel_layer)
        print('channel name is...', self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            'programmers',
            self.channel_name
        )
        raise StopConsumer()
    







class asconsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })
        print('connected')
        await (self.channel_layer.group_add)(
            'programmers',
            self.channel_name
        )
        print('channel name......',self.channel_name)
    async def websocket_receive(self, event):

        message = event['text']
        print(message)
        await self.channel_layer.group_send(    
        'programmers',
        {
            'type':'chat.message',
            'message':event['text']
        })
    async def chat_message(self, event):
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })
    async def websocket_disconnect(self, event):
        print("connection disconnected...", event)
        print('channel layer is...', self.channel_layer)
        print('channel name is...', self.channel_name)
        await self.channel_layer.group_discard(
            'programmers',
            self.channel_name
        )
        raise StopConsumer()
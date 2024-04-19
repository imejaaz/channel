from django.contrib import admin
from .models import messages, group
# Register your models here.
admin.site.register(group)
admin.site.register(messages)
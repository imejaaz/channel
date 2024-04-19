from django.shortcuts import render
from django.http import HttpResponse
from .models import group, messages



def index(request, group_name):
    
    GroupName = group_name
    GroupExist = group.objects.filter(name = GroupName).first()
    if GroupExist:
        chat = messages.objects.filter(group = GroupExist)
    else:
        GroupObject = group(name = GroupName)
        GroupObject.save()
    return render(request, 'app/index.html',{'group':group_name, 'chat':chat})
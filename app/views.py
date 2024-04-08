from django.shortcuts import render
from django.http import HttpResponse
def index(request, group_name):
    
    return render(request, 'app/index.html',{'group':group_name})
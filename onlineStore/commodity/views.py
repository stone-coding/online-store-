from django.shortcuts import render

# Create your views here.

"""
view 
view the python function
two requirements:
First, parameter is receiving the requests. this request is an object of HttpRequest
Second, must return a response
"""
# request
# from django.http import HttpRequest
from django.http import HttpResponse

# we hope user type http://127.0.0.1:8000/index/ to visit our website
def index(request):

    return HttpResponse('ok')

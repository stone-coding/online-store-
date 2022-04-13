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
# 导入HttpResponse模块
from django.http import HttpResponse
# 导入render模块
from django.shortcuts import render

# we hope user type http://127.0.0.1:8000/index/ to visit our website
def index(request):

    # return HttpResponse('ok')
    # context = {'title':'test model data'}

    #模拟数据查询
    context={
        'name':'马上双11,点击有惊喜'
    }

    return render(request, 'Commodity/index.html', context = context)

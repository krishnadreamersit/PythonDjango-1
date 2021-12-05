from django.http import HttpResponse
from . import functions

def index(request):
    return HttpResponse("Hello from index") # Browser

def home(request):
    return HttpResponse("Hello from home") # Browser

def add(request):
    num1 = 45
    num2 = 43
    # num3 = num1 + num2
    num3 = functions.doAdd(num1, num2)
    return HttpResponse("Sum = "+str(num3)) # Browser
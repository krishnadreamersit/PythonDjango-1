from django.shortcuts import render
from django.http import  HttpResponse
from . import models

# Create your views here.

def index(request):
    # Step-1
    # person1 = models.Person()
    # person1.pid=2
    # person1.fullname='Raj Rai'
    # person1.contactaddress='Bhk'
    # person1.save()

    # Step-2
    person2 = models.Person(pid=3, fullname='Raju', contactaddress='LAT')
    person2.save()
    return HttpResponse("Hello from app7")

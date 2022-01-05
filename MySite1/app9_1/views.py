from django.shortcuts import render
from .forms import PersonForm

# Create your views here.


def index(request): # display form
    form1 = PersonForm()
    return render(request, 'app9_1/form1.html', {'f1':form1})


def getForm(request): # get values from form
    fname = request.GET.get('full_name')
    caddress = request.GET.get('contact_address')
    print(fname, caddress)
    context = {
        'full_name':fname,
        'contact_address':caddress,
    }
    return render(request, 'app9_1/display1.html', context)
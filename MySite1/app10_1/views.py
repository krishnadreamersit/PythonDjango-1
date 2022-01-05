from django.shortcuts import render
from .forms import PersonModelForm

# Create your views here.
def displayform(request):
    form1 = PersonModelForm()
    if request.method == 'GET':
        return render(request, 'app10_1/form1.html', {'f1':form1})
    else:
        form1 = PersonModelForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, 'app10_1/display1.html', {'status':True})


from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    #update existing user
    # username=admin
    # password=admin
    # email=admin@gmail.com
    # first_name=''
    # last_name=''
    # user1 = User.objects.get(username='admin')
    # print(user1.username, user1.password, user1.email, user1.first_name, user1.last_name, user1.is_superuser)
    # user1.first_name="Krishna"
    # user1.last_name="Aryal"
    # user1.save()
    # print(user1.first_name, user1.last_name)
    # return HttpResponse("Hello from app12_1")

    if request.method=='GET':
        return render(request, 'app12_1/form1.html') # display login form
    else: # POST
        un = request.POST.get('txtUser')
        pw = request.POST.get('txtPassword')
        # do login
        result = authenticate(username=un, password=pw)
        if (result):
            user1 = User.objects.get(username=un)
            print("TRUE")
            return render(request, 'app12_1/display1.html', {'user':user1})
        else:
            return render(request, 'app12_1/form1.html') # display login form

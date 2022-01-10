from django.shortcuts import render
from django.contrib.auth.models import User # System Defined
from django.contrib.auth import authenticate

def index(request):
    # if request.method =='POST':
    #     user = request.POST.get('txt_user')
    #     password = request.POST.get('txt_password')
    #     if user =='krishna' and password == 'krishna@123':
    #         request.session['user'] = user # Create session - krishna
    #         return render(request, 'app12_1/display_result.html', {'user': user, 'flag': True})
    # return render(request, 'app12_1/login.html')

    if request.method =='POST':
        user = request.POST.get('txt_user')
        password = request.POST.get('txt_password')
        user1 = authenticate(username=user, password=password)
        if user1 is not None:
            request.session['user'] = user # Create session
            return render(request, 'app12_1/display_result.html', {'user': user, 'flag': True})
        else:
            return render(request, 'app12_1/login.html')
    else:
        return render(request, 'app12_1/login.html')

def check_session(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'app12_1/display_result.html', {'user': user, 'flag': True})
    else:
        return render(request, 'app12_1/display_result.html', {'user': 'NA', 'flag': False})


def check_session2(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'app12_1/display_result.html', {'user': user, 'flag': True})
    else:
        return render(request, 'app12_1/display_result.html', {'user': 'NA', 'flag': False})
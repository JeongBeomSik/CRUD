from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')    

def create(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('login')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('base')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')    

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('base')

    return render(request, 'login.html')


def profile_update(request):
    profile = Profile.objects.get(user=request.user)
    context = {"profile":profile}
    return render(request,'profile_update.html',context)
    

def update_profile(request):
    if request.method == 'POST':
        profile = Profile()
        nickname = request.POST['nickname']
        introduction = request.POST['introduction']
        profile.nickname = nickname
        profile.introduction = introduction
        profile.user = request.user
        profile.save()
        return render(request,'base.html')
    
    else: return render(request,'profile_update.html')
    
   
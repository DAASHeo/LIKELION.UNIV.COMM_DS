from contextlib import redirect_stdout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import signupForm
# Create your views here.
def login(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        user = authenticate(request=request, username=username, password1=password1)
        if user is not None:
            auth.login(request, user)
        return redirect('board')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect("board")

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request,user)
            return redirect('mypage')
        return redirect('signup')
    else:
        form = signupForm()
        return render(request, 'signup.html',{'form':form})
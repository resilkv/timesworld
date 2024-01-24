from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm
from .models import Users
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):

    if request.method == 'POST':
   
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html',{'role':user.role})



def logout_view(request):
    logout(request)

    return redirect('/')  
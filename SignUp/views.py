#from django.shortcuts import render #, redirect
#from SignUp.forms import UserRegisterForm
#from django.contrib.auth import login, authenticate
#from django.contrib import messages

#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.

#def signup(request):
 #   if request.method =='POST':
 #       form = UserCreationForm(request.POST)
 #       if form.is_valid():
  #          user = form.save()
  #          login(request, user)
  #          return redirect('home')
        
  #  else:
  #      form = UserCreationForm()
  #  return render(request, 'SignUp/templates/signup.html', {'form': form})

#@login_required
#def home(request):
 #   return render(request, 'SignUp/templates/home.html')

#def register_view(request):
      
#      if request.method == 'POST':
 #           form = UserRegisterForm(request.POST or NONE)
 #           if form.is_valid():
 #                 new_user = form.save()
#username = form.cleaned_data.get('username'), Your account was created successfully
 #                 new_user = authenticate(username=form.cleaned_data['email'], 
 #                                         password=form.cleaned_data['password1']
  #                )

 #                 login(request, new_user )
  #                return redirect('core:index')
#    else:
  #          print("User cannot be registered")
  #          form = UserRegisterForm()

  #    context = {
   #         'form': form
#}
  #    return render(request, "SignUp/signup.html", context)

  # SignUp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from rest_framework.views import APIView


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('SignUp:login')
    else:
        form = RegisterForm()
    return render(request, 'SignUp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'SignUp/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

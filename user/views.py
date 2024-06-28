import cloudinary.uploader
from django.shortcuts import render, redirect
from . forms import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
import cloudinary

# Create your views here.
# ////// Registration
def registration(request):
     if request.method == "POST":
          form = UserProfile(request.POST, request.FILES)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               email = form.cleaned_data.get('email')
               password = form.cleaned_data.get('password1')
               userImage = form.cleaned_data.get('userImage')
               cloudinary.uploader.upload(userImage)
               
               
               # If the user Email Already Exist
               if form.cleaned_data['userImage'] == " ":
                    messages.error(request, "Please upload your profile picture")
                    return redirect('register')
               
               elif User.objects.filter(Q(email = email)).exists():
                    messages.warning(request, "This Email Has Been Regsitered Before")
                    return redirect('register')
               else:
                    user = User.objects.create_user(username, email, password)
                    form = form.save(commit=False)
                    form.user = user
                    form.save()
                    messages.success(request, "User Regiestered Successfully")
                    login(request, user)
                    return redirect('home')
               
          else: 
               messages.warning(request, "Error Registering User")
               
     context = {
          'form': UserProfile
     }
     return render(request, 'user/register.html', context)



# ////// Login
def user_login(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
               login(request, user)
               messages.success(request, f"User {username} is Logged in Successfully")
               return redirect('home')
          else:
               messages.warning(request, "Wrong Username or Password")
               return redirect('login')
          
     return render(request, 'user/login.html')


def user_logout(request):
     logout(request)
     messages.warning(request, "User Logout Successfully")
     return redirect('home')
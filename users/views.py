from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from posts.models import Post
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:post_list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user =authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'you are now logged in as {username}.')
                return redirect("posts:post_list")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm
        return render(request, 'users/login.html', {"form": form})
    



def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("homepage")
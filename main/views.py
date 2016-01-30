from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import LoginForm


def index_view(request):
    if request.user.is_authenticated():
        return render(request, 'index.html', {'username': request.user.username,
         'is_admin': request.user.is_staff, 'motd': "herrrrp, derp"})
    else:
        return render(request, 'index.html')


def post_view(request):
    if request.user.is_authenticated():
        return render(request, 'post.html', {'username': request.user.username})
    else:
        return redirect('login')


def account_view(request):
    if request.user.is_authenticated():
        return render(request, 'account.html', {'username': request.user.username,
            'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name,
            'last_login': request.user.last_login, 'is_admin': request.user.is_staff})
    else:
        return redirect('login')

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = authenticate(username=username, password=password)

    if request.method == 'POST':
        if user is not None:
            if user.is_active:
                # User is valid, active and authenticated
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error_message': "The password is valid, but the account has been disabled!"})
        else:
            # the authentication system was unable to verify the username and password
            return render(request, 'login.html', {'error_message': "The username and password were incorrect."})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def test_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            redirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'testing.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from .models import Post
from django.contrib.auth.models import User


def index_view(request):
    post_results = Post.objects.all().order_by('-post_date')

    if request.user.is_authenticated():
        return render(request, 'index.html', {'username': request.user.username,
            'is_admin': request.user.is_staff, 'post_results': post_results})
    else:
        return render(request, 'index.html', {'post_results': post_results})


def post_view(request):
    if request.user.is_authenticated():
        return render(request, 'post.html', {'username': request.user.username,
            'is_admin': request.user.is_staff})
    else:
        return redirect('login')


def account_view(request):
    if request.user.is_authenticated():
        return render(request, 'account.html', {'username': request.user.username,
            'is_admin': request.user.is_staff})
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

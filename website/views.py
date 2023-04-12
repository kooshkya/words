from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from . import my_utils as mu

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "website/index.html")
    else:
        return HttpResponseRedirect(reverse('website:login'))


def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("website:index"))
        else:
            context['errors'] = ["Your login credentials are invalid."]
    return render(request, "website/login.html", context=context)


def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "Username already exists!", fail_silently=True)
        elif password1 != password2:
            messages.add_message(request, messages.ERROR, "Passwords do not match", fail_silently=True)
        elif not mu.isPasswordSafe(password1):
            messages.error(request, "Password is not secure.")
        else:
            user = User.objects.create_user(username, email, password1, first_name=first_name, last_name=last_name)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("website:index"))

    return render(request, "website/register.html")


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse("website:index"))


def add_word(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "website/add_word.html", context={})
        else:
            return HttpResponseRedirect(reverse("webite:index"))
    else:
        pass
    
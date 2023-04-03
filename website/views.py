from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "website/index.html")
    else:
        return HttpResponseRedirect(reverse('website:login'))

def login_user(request):
    context = {}
    if request.method == "POST":
        # process login attempt
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
    return HttpResponse("register page placeholder")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse("website:index"))
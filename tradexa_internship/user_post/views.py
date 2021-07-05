from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def index(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("create-post")
        else:
            messages.error(request, "Wrong Credentials!")
    return redirect('/')


def register(request):
    if request.method == "POST":
        username = request.POST.get('uname', None)
        password = request.POST.get('password', None)
        fname = request.POST.get('fname', None)
        lname = request.POST.get('lname', None)
        email = request.POST.get('email', None)

        if User.objects.filter(Q(email=email) | Q(username=username)).exists():
            messages.error(request, "Email or username is already taken!")
            return redirect("/")
        user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password)
        user.save()
        auth.login(request, user)
        return redirect("create-post")
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect("/")
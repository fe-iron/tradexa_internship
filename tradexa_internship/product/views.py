from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product
from user_post.models import Post
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/')
def post_create(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        pname = request.POST.get('pname', None)
        weight = request.POST.get('weight')
        price = request.POST.get('price', None)
        message = request.POST.get('message', None)
        prod = Product(name=pname, weight=weight, price=price)
        prod.save()

        user = request.user
        user = User.objects.get(username=user)
        p_ost = Post(user=user.email, text=message)
        p_ost.save()
        message.info(request, "Successfully created!")

    return redirect("create-post")
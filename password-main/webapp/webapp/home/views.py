from random import random
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
import os
import random
from .sendEmail import *


def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

# Create your views here.
def home(request):
    return render(request, 'index.html')

def homesignup(request):
    l = os.listdir('home/static/home/img/images/')
    l = to_matrix(l,5)

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        img1 = request.POST['img1']
        img2 = request.POST['img2']
        img3 = request.POST['img3']
        img4 = request.POST['img4']
        img5 = request.POST['img5']

        user = User.objects.create_user(username=username, email=email, password=password)
        p = Password1(user=user, img1=img1, img2=img2, img3=img3, img4=img4, img5=img5)
        p.save()
        return render(request, 'signup.html', {'data': l, 'res': 'Signup Sucessful'})
    return render(request, 'signup.html', {'data': l})



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        img1 = request.POST['img1']
        img2 = request.POST['img2']
        img3 = request.POST['img3']
        img4 = request.POST['img4']
        img5 = request.POST['img5']

        user = authenticate(username=username,password=password)
        if user is not None and len(Password1.objects.filter(user=user, img1=img1, img2=img2, img3=img3, img4=img4, img5=img5)) != 0:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('home')


def homesignin(request):
    l = os.listdir('home/static/home/img/images/')
    random.shuffle(l)
    l = to_matrix(l,5)
    return render(request, 'signin.html', {'data': l})


def dashboard(request):
    return render(request, 'dashboard.html')


def homeforgot(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email)[0]
        message = """\
        Subject: Forgot Password

        Pls click on this link to reset localhost:8000/forgot?id="""+str(user.id)
        send(message, "abhijeetsasmal74@gmail.com")
    return render(request, 'homeforgot.html')

def forgot(request):
    l = os.listdir('home/static/home/img/images/')
    l = to_matrix(l,5)
    id = ""
    if request.method == 'GET':
        id = request.GET['id']
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        img1 = request.POST['img1']
        img2 = request.POST['img2']
        img3 = request.POST['img3']
        img4 = request.POST['img4']
        img5 = request.POST['img5']

        user = User.objects.filter(id=id)
        user.password = password
        user.save()
        p = Password1(user=user, img1=img1, img2=img2, img3=img3, img4=img4, img5=img5)
        p.save()
        return render(request, 'forgot.html', {'data': l, 'res': 'Changed Password Sucessful'})
    return render(request, 'forgot.html', {'data': l, 'id': id})
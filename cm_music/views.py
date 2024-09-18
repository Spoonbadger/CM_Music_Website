from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import random

from .models import User, Post

def bio(request):
    return render(request, "cm_music/bio.html")


def contact(request):
    return render(request, "cm_music/contact.html")


def index(request):
    videos = [
        '/videos/By Acting Together We Really Act Vert SD Craig Morley copy.mp4',
        '/videos/LMM 32 secs VERT.mp4',
        '/videos/Ocean of Love VERT SD Craig Morley copy.mp4',
        '/videos/Shotgun when 12 VERT SD Craig Morley copy.mp4',
        '/videos/VERT cm Beauty and Loss.mp4',
        '/videos/VERT dune one.mp4',
        '/videos/VERT Firewing.mp4',
        '/videos/VERT On the coarctation.mp4',
        '/videos/VERT2 cig thrown.mp4'
    ]

    random.shuffle(videos)
    
    return render(request, 'cm_music/index.html', {
        'videos': videos,
        })


def links(request):
    return render(request, "cm_music/links.html")


def music(request):
    return render(request, "cm_music/music.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, 'login.html', {
                "message": "Invalid username and/or password."
            })
        
    else:
        return render(request, 'cm_music/login.html')
        


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'cm_music/register', {
                "message": "Password and Password confirmation must match."
            })
        
        # Attempt to create a new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'cm_music/register', {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse(index))
    
    else:
        return render(request, 'cm_music/register.html')
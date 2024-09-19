from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import contactForm
from .models import Contact

import random

from .models import User

def bio(request):
    return render(request, "cm_music/bio.html")



def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Create the new Contact and save it
            contact = Contact(name=name, email=email, message=message)
            contact.save()

            # Also send an email
            send_mail(
                'New music contact form message', # Subject
                f"Name: {name}\n Message: {message}", #
                email,
                ['craig.adam.morley@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'cm_music/thankyou.html')
        else:
            return render(request, 'cm_music/contact.html', {
                "form": form,
            })
    else:
        return render(request, "cm_music/contact.html", {
            "form": contactForm(),
        })


def index(request):

    return render(request, 'cm_music/index.html')


def links(request):
    return render(request, "cm_music/links.html")


def music(request):
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

    return render(request, "cm_music/music.html", {
        "videos": videos,
    })


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
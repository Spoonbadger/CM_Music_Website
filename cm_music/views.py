from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

import random

from .forms import contactForm
from .models import ContactMessage, Videos


def index(request):
    return render(request, 'cm_music/index.html')


def bio(request):
    return render(request, "cm_music/bio.html")


def contact_page(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Create the new ContactMessage and save it
            contact = ContactMessage(name=name, email=email, message=message)
            contact.save()

            # Send an email, I can't beleive this works!
            send_mail(
                'New music Contact Form message', # Subject line
                f"Name: {name}\n Message: {message}", # Displayed in email body
                email,  # Email message displayed in email body
                ['craig.adam.morley@gmail.com'], # Send to address
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
    

def invest(request):
    return render(request, "cm_music/invest.html")


def links(request):
    return render(request, "cm_music/links.html")


def music(request):
    videos = list(Videos.objects.all())
    random.shuffle(videos)

    return render(request, "cm_music/music.html", {
        "videos": videos,
    })


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse(index))
#         else:
#             return render(request, 'login.html', {
#                 "message": "Invalid username and/or password."
#             })
        
#     else:
#         return render(request, 'cm_music/login.html')
        


# def logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse(index))


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']

#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         if password != confirm_password:
#             return render(request, 'cm_music/register', {
#                 "message": "Password and Password confirmation must match."
#             })
        
#         # Attempt to create a new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.save()
#         except IntegrityError:
#             return render(request, 'cm_music/register', {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse(index))
    
#     else:
#         return render(request, 'cm_music/register.html')
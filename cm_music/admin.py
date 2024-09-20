from django.contrib import admin

# Register your models here.
from .models import ContactMessage, Videos


admin.site.register(ContactMessage)
admin.site.register(Videos)
from django import forms
from django.core.validators import EmailValidator


# Client-side validation
class contactForm(forms.Form):
    name = forms.CharField(label="Name: ", max_length=108, min_length=1)
    email = forms.EmailField(validators=[EmailValidator], label="Email: ", min_length=5)
    message = forms.CharField(label="Message: ", widget = forms.Textarea)
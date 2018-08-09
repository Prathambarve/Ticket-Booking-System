from django import forms
from .models import User
from django.forms import ModelForm, PasswordInput
try:
    from captcha.fields import ReCaptchaField # Recaptcha
except:
    print ('Perform    "pip install django-recaptcha"')

class RegisterForm(forms.Form):
    fname = forms.CharField(max_length="15", required=True)
    lname = forms.CharField(max_length="15", required=True)    
    email = forms.EmailField(required=True)
    password = forms.CharField(widget = PasswordInput(), required=True)
    #captcha = ReCaptchaField() # Recaptcha validation field

class LoginForm(forms.Form):
    email = forms.EmailField(label='', required=True)
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput())
    # class Meta:
    #     model = User
    #     exclude = ('name',)
    #     widgets = {
    #             'email': forms.TextInput(attrs={'placeholder':'abc@mail.com'}),
    #             'password': forms.TextInput(attrs={'placeholder':'password'})
    #     }

    
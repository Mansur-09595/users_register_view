from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from captcha.fields import ReCaptchaField
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    captcha = ReCaptchaField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone', 'captcha',)
        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone',)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django import forms
from captcha.fields import ReCaptchaField


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

class CustomUser(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=False, null=True,)
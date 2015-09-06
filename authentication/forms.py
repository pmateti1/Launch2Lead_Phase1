__author__ = 'Kovas3'

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from authentication.models import UserProfile

class RegistrationForm(ModelForm):
    username = forms.CharField(help_text="Please Enter a Name")
    email = forms.EmailField(help_text="Please Enter your Email")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please Enter a Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text="Verify Password")

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, Please try registering by a different username")

    def clean(self):
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                    raise forms.ValidationError("The passwords did not match.  Please try again.")
            return self.cleaned_data
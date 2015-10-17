__author__ = 'Kovas3'

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from authentication.models import UserProfile


class LoginForm(forms.Form):
    email = forms.CharField(label=(u'Email'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        fields = ['email', 'password']


class RegistrationForm(ModelForm):
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))
    password = forms.CharField(widget=forms.PasswordInput(), label=(u'Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(), label=(u'Verify Password'))

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'password2')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     try:
    #         User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         return username
    #     raise forms.ValidationError("That username is already taken, Please try registering by a different username")
    #
    # def clean_email(self):
    #     data = self.cleaned_data['email']
    #     if "@" not in data:
    #         raise forms.ValidationError("Email Address not valid")
    #     return data

    # def clean(self):
    #     if self.cleaned_data['password'] != self.cleaned_data['password2']:
    #         raise forms.ValidationError("The passwords did not match.  Please try again.")
    #     return self.cleaned_data

    def save(self, commit=True):
        UserProfile = super(RegistrationForm, self).save(commit=False)
        UserProfile.set_password(self.cleaned_data['password'])
        if commit:
            UserProfile.save()
        return UserProfile
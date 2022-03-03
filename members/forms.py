"""
forms.py contains classes to work with Sign-in and Profile forms.
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from book.models import Profile


class SignUpForm(UserCreationForm):
    """
    A class represents Sign in form.
    """
    username = forms.CharField(max_length=30, label="Username",
                               widget=forms.TextInput(attrs={'class': 'form-control col-3', "id": "username"}))
    email = forms.EmailField(max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control col-3', "id": "email"}))
    first_name = forms.CharField(max_length=30, label="First name",
                                 widget=forms.TextInput(attrs={'class': 'form-control col-3', "id": "first_name"}))
    last_name = forms.CharField(max_length=30, label="Last name",
                                widget=forms.TextInput(attrs={'class': 'form-control col-3', "id": "last_name"}))
    password1 = forms.CharField(max_length=30, label="Password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control col-3', "id": "password1"}))
    password2 = forms.CharField(max_length=30, label="Confirm password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control col-3', "id": "password2"}))

    class Meta:
        """
         Class container with some options (metadata) attached to the model.
         """
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password (self):
        """
        This function checks is the entered password and re-confirmed password matches.
        If the passwords mathes the function returns as below.
        :return: password2
        :rtype: str
        Otherwise the function raises exception.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("The given passwords do not match")
        return password2

    def clean_email (self):
        """
        This function checks if the given email exists in the DB.
        If such email does not exist in the db returns as below.
        :return: email
        :rtype: str

        Otherwise it throws exception.
        """
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already taken")
        return email

    def clean_username (self):
        """
        This function checks if the given username exists in the DB.
        If such username does not exist in the db returns as below.
        :return: username
        :rtype: str

        Otherwise it throws exception.
        """
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This username is already taken")
        return username


class ProfilePageForm(forms.ModelForm):
    """
    A class represents a user profile form.
    """

    class Meta:
        """
         Class container with some options (metadata) attached to the model.
        """
        model = Profile
        fields = ('user', 'phone', 'country', 'city', 'street', 'housenumber')
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'id', 'type': 'hidden'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'housenumber': forms.NumberInput(attrs={'class': 'form-control'}),
        }

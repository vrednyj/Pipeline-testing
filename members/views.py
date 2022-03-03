"""
utils.py contains classes that work with user registration forms.
"""

from django.urls import reverse_lazy
from django.views import generic

from book.models import Profile
from . import forms
from .forms import ProfilePageForm


# Create your views here.
class UserRegisterView(generic.CreateView):
    """
    A class to generate sign in form.
    """
    form_class = forms.SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class CreateProfilePageView(generic.CreateView):
    """
    A class to generate profile page with empty fields.
    This is for first time registered users.
    """
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/add_profile.html'
    success_url = reverse_lazy('home')


class EditProfilePageView(generic.UpdateView):
    """
    A class to generate profile page.
    """
    model = Profile
    template_name = 'registration/edit_profile.html'
    form_class = ProfilePageForm
    success_url = reverse_lazy('home')

    def get_object(self):
        """
        :return: <class 'book.models.Profile'>
        :rtype: object
        """
        user = self.request.user
        return Profile.objects.get(user=user.id)

from django.urls import path
from .views import UserRegisterView, CreateProfilePageView, EditProfilePageView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('add_profile/', CreateProfilePageView.as_view(), name="add_profile"),
    path('edit_profile/', EditProfilePageView.as_view(), name="edit_profile"),

]

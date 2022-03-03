"""
Urls.py works the same as that of the urls.py in the project file structure.
The primary aim being, linking the user’s URL request to the corresponding pages it is pointing to.
You won’t find this under the app files.
We create this by clicking on the New file option written on the top, after the Project name.
"""

from django.urls import path

from book.views import AddAttraction, Home, CurrentTrip, CalendarView, Book, BookEdit, BookDelete, YourBooking

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('item/<int:pk>/', CurrentTrip.as_view(), name='item'),
    path('book/<int:pk>/', Book.as_view(), name='book'),
    path('booking_edit/<int:pk>/', BookEdit.as_view(), name='booking_edit'),
    path('delete_booking/<int:pk>/', BookDelete.as_view(), name='booking_delete'),
    path('calendar/<int:pk>/', CalendarView.as_view(), name='calendar'),
    path('your_booking/<int:pk>/', YourBooking.as_view(), name='your_booking'),
    path('add_attraction/', AddAttraction.as_view(), name='add_attraction'),
]

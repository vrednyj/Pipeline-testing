"""
Views are also an important part when we talk about the Django app structure.
Views provide an interface through which a user interacts with a Django web application.
It contains all the views in the form of classes.
We use the concept of Serializers in Django Rest_Framework for making different types of views.
Some of these are CustomFilter Views, Class-Based List Views, and Detail Views.
"""

from book.models import Profile, Attraction, Booking
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .filters import Filters
#
from .forms import BookingForm, AddAttractionForm
from datetime import datetime
from datetime import timedelta
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from .utils import Calendar


class CalendarView(generic.ListView):
    """
    A class to create calendar page.
    """
    model = Booking
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        """
        :param kwargs:
        :type kwargs:
        :return: the name of attraction.
        :rtype: dict "example {'title': 'Halloween Roller'}"
        """
        context = super().get_context_data(**kwargs)
        # get attractions from logged attraction agency
        location = self.kwargs['pk']
        attractions_in_location = Attraction.objects.filter(location=self.kwargs['pk'])
        attractions = []
        for attraction in attractions_in_location:
            attractions.append(attraction)
        # get today date
        date = datetime.today()
        calendar = Calendar(date.year, date.month, attractions)
        # call the formatmonth method, which returns our calendar as a table
        html_calendar = calendar.formatmonth(withyear=True)
        # own html templates is trusted, about 'html_calendar'
        context['calendar'] = mark_safe(html_calendar)
        return context


class Book(generic.CreateView):
    """
    The class to generate a booking form for the attraction.
    """
    model = Booking
    form_class = BookingForm
    template_name = 'book.html'
    success_url = reverse_lazy('home')

    def get_initial(self, *args, **kwargs):
        """
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return: the name of attraction.
        :rtype: dict "example {'title': 'Halloween Roller'}"
        """
        initial = {}
        title = Attraction.objects.get(id=self.kwargs['pk'])
        initial['title'] = title.title
        return initial


class BookEdit(generic.UpdateView):
    """
    A class to generate booking edit form.
    """
    model = Booking
    template_name = 'booking_edit.html'
    form_class = BookingForm
    success_url = reverse_lazy('home')


class YourBooking(generic.ListView):
    """
    A class do present the Current bookings of a user
    """

    model = Booking
    template_name = 'your_booking.html'

    def get_context_data(self, *args, **kwargs)-> object:
        """
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return: Bookings of a user exmp. <QuerySet [<Booking:
        Paradise Peer | test1>, <Booking: Wicker Roller Coaster | test1>]>
        :rtype: object <class 'django.db.models.query.QuerySet'>
        """
        context = {}
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        book = Booking.objects.filter(user=page_user.user)
        context["book"] = book
        return context


class BookDelete(generic.DeleteView):
    """
    A class to generate booking deletion form.
    """
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('home')


class Home(generic.ListView):
    """
    Class for to represent home page.
    """
    model = Attraction
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> object:
        """
        :param kwargs:
        :type kwargs:
        :return: <book.filters.Filters object at "object id">
        :rtype: object
        """
        context = super().get_context_data(**kwargs)
        context['filter'] = Filters(self.request.GET, queryset=self.get_queryset())
        return context


class CurrentTrip(generic.DetailView):
    """
    A class to generate current trip page.
    """
    model = Attraction
    template_name = 'currenttrip.html'


class AddAttraction(generic.CreateView):
    """
    A class for a form to Add new attractions
    """
    # check this view
    model = Attraction
    form_class = AddAttractionForm
    template_name = 'addattraction.html'
    success_url = reverse_lazy('home')

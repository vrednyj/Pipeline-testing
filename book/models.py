"""
Models.py represents the models of web applications in the form of classes.
It is considered the most important aspect of the App file structure.
Models define the structure of the database. It tells about the actual design,
relationships between the data sets, and their attribute constraints.
"""

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Location(models.Model):
    """
    A class represents the location of the

    Attributes
    ----------
    name : str
        name of the attraction
    city : str
        name of the city
    user : Any
        month of the user

    """
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Attraction(models.Model):
    """
    Attributes
    ----------
    title : str
        name of the attraction
    image : object
        image of the attraction
    location : str
        month of the user
    body : str
        name of the attraction
    price : float
        name of the city
    min_height : str
        month of the user
    max_weight : str
        month of the user

    """

    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    min_height = models.CharField(max_length=100, default='1.2M')
    max_weight = models.CharField(max_length=100, default='120KG')

    def __str__(self):
        return str(self.title) + ' | ' + str(self.location)


class Profile(models.Model):
    """
    A class represents registered users profile

    Attributes
    ----------
    user : str
        name of the user
    phone : int
        phone number
    country : str
        country of the user location
    city : str
        city of the user location
    street : str
        name of the user street
    housenumber : int
        number of the house
    """

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)  # +353 phone format is not allowed
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    housenumber = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Booking(models.Model):
    """
    A class represents a Booking

    Attributes
    ----------
    user : Any
        name of the user
    title : Any
        year of the calendar
    start_time : Any
        month of the calendar

    Methods
    -------
    get_html_title:
        returns string of its title + user name.

    """
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()

    @property
    def __str__(self):
        """
        Returns str(self).
        """
        return str(self.title) + ' | ' + str(self.user)

    @property
    def get_html_title(self):
        """
        :return:
        :rtype: str
        """
        return str(self.title) + ' | ' + str(self.user)

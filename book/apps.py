"""
Apps.py is a file that is used to help the user include the application configuration for their app.
Users can configure the attributes of their application using the apps.py file.
However, configuring the attributes is a rare task a user ever performs,
because most of the time the default configuration is sufficient enough to work with.
"""

from django.apps import AppConfig


class BookConfig(AppConfig):
    """
    BookingConfig class with inherited AppConfig Class representing a Django application and its configuration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'

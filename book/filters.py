import django_filters
from .models import Attraction


class Filters(django_filters.FilterSet):
    """
    A class to represent Filters for attractions.
    """
    class Meta:
        """
        Class container with some options (metadata) attached to the model.
        """
        model = Attraction
        fields = {
            'title': ['icontains'],
        }

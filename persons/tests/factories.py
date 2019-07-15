import factory

from persons.models import Person
from persons.models import Alias


class PersonFactory(factory.DjangoModelFactory):
    """
        Define Person Factory
    """
    class Meta:
        model = Person


class AliasFactory(factory.DjangoModelFactory):
    """
        Define Alias Factory
    """
    class Meta:
        model = Alias

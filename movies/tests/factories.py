import factory

from movies.models import Movie


class MovieFactory(factory.DjangoModelFactory):
    """
        Define Movie Factory
    """
    class Meta:
        model = Movie

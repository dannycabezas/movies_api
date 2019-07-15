import datetime

from .utils import int_to_roman
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


def current_year():
    return datetime.date.today().year


class MovieActor(models.Model):
    """
        M2M for movie casting
    """
    movie = models.ForeignKey('movies.Movie', on_delete=models.PROTECT)
    person = models.ForeignKey('persons.Person', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "MovieActor"
        verbose_name_plural = "MovieActors"
        db_table = "movie_actor"


class MovieDirector(models.Model):
    """
        M2M for movie directors
    """
    movie = models.ForeignKey('movies.Movie', on_delete=models.PROTECT)
    person = models.ForeignKey('persons.Person', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "MovieDirector"
        verbose_name_plural = "MovieDirectors"
        db_table = "movie_director"


class MovieProducer(models.Model):
    """
        M2M for movie producers
    """
    movie = models.ForeignKey('movies.Movie', on_delete=models.PROTECT)
    person = models.ForeignKey('persons.Person', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "MovieProducer"
        verbose_name_plural = "MovieProducers"
        db_table = "movie_producer"


class Movie(models.Model):
    title = models.CharField(max_length=240)
    release_year = models.IntegerField(validators=[
        MinValueValidator(1984),
        MaxValueValidator(current_year)
    ]
    )
    directors = models.ManyToManyField('persons.Person',
                                       through='movies.MovieDirector',
                                       related_name='movies_as_director')
    casting = models.ManyToManyField('persons.Person',
                                     through='movies.MovieActor',
                                     related_name='movies_as_actor')
    producers = models.ManyToManyField('persons.Person',
                                       through='movies.MovieProducer',
                                       related_name='movies_as_producer')

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        db_table = "movie"

    def __str__(self):
        return self.title

    def _get_full_names_string(self, model):
        return '|'.join([
            '{0} {1}'.format(
                item.person.first_name,
                item.person.last_name
            ) for item in model.objects.filter(movie=self)
        ])

    @property
    def get_casting(self):
        return self._get_full_names_string(MovieActor)

    @property
    def get_producers(self):
        return self._get_full_names_string(MovieProducer)

    @property
    def get_directors(self):
        return self._get_full_names_string(MovieDirector)

    @property
    def get_release_year(self):
        return int_to_roman(self.release_year)

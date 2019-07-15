import pytest

from movies.tests.factories import MovieFactory
from persons.tests.factories import PersonFactory


@pytest.mark.django_db
def test_movie_model():
    """ Test movie model """
    # create movie model instance
    title = 'Test movie title'
    release_year = 2019
    actor_name = "Danny"
    producer_name = "Producer"
    director_name = "Director"
    gender = "M"
    last_name = "Cabezas"
    role = "A"
    actor = PersonFactory(
        gender=gender,
        first_name=actor_name,
        last_name=last_name,
        role=role,
    )
    director = PersonFactory(
        gender=gender,
        first_name=actor_name,
        last_name=director_name,
        role=role,
    )
    producer = PersonFactory(
        gender=gender,
        first_name=actor_name,
        last_name=producer_name,
        role=role,
    )

    movie = MovieFactory(
        title=title,
        release_year=release_year,
    )
    movie.casting.add(actor)
    movie.directors.add(director)
    movie.producers.add(producer)

    assert movie.title == title
    assert movie.release_year == release_year
    assert movie.get_casting == "Danny Cabezas"
    assert movie.get_producers == "Danny Producer"
    assert movie.get_directors == "Danny Director"

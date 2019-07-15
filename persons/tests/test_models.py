import pytest

from persons.tests.factories import AliasFactory
from persons.tests.factories import PersonFactory


@pytest.mark.django_db
def test_alias_model():
    """ Test content rating model """
    # create content rating model instance
    name = 'Test alias'
    gender = "M"
    first_name = "Danny"
    last_name = "Cabezas"
    role = "A"
    person = PersonFactory(
        gender=gender,
        first_name=first_name,
        last_name=last_name,
        role=role,
    )
    alias = AliasFactory(
        name=name,
        persons=person
    )
    assert alias.name == name


@pytest.mark.django_db
def test_person_model():
    """Test person model. """
    gender = "M"
    first_name = "Danny"
    last_name = "Cabezas"
    role = "A"
    person = PersonFactory(
        gender=gender,
        first_name=first_name,
        last_name=last_name,
        role=role,
    )
    assert person.first_name == first_name
    assert person.last_name == last_name
    assert person.role == role
    assert person.gender == gender

from django.db import models
from persons.choices import GENDERS
from persons.choices import ROLES


class Alias(models.Model):
    """
        Model for Alias
    """
    name = models.CharField(max_length=240)
    persons = models.ForeignKey('persons.Person',
                                on_delete=models.PROTECT,
                                related_name='aliases')

    class Meta:
        verbose_name = "Alias"
        verbose_name_plural = "Aliases"
        db_table = "alias"

    def __str__(self):
        return self.name


class Person(models.Model):
    """
        Model for Person
    """
    gender = models.CharField(choices=GENDERS, max_length=1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(choices=ROLES, max_length=1)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        db_table = "person"

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_aliases(self):
        return ','.join(
            [
                '{0}'.format(
                    alias.name,
                )
                for alias in self.aliases.all()
            ]
        )

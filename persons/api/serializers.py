from persons.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    aliases = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    def get_aliases(self, person):
        return ','.join(
            [
                '{0}'.format(
                    alias.name,
                )
                for alias in person.aliases.all()
            ]
        )


class PersonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
            'gender',
            'role'
        ]


class PersonUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = [
            'role'
        ]

from movies.models import Movie
from rest_framework import serializers
from persons.api.serializers import PersonSerializer


class MovieSerializer(serializers.ModelSerializer):
    directors = PersonSerializer(many=True, read_only=True)
    casting = PersonSerializer(many=True, read_only=True)
    producers = PersonSerializer(many=True, read_only=True)
    release_year = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_release_year(self, movie):
        return movie.get_release_year


class MovieCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title', "release_year"]

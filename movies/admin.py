from django.contrib import admin
from movies.models import Movie
from movies.models import MovieActor
from movies.models import MovieDirector
from movies.models import MovieProducer


class MovieActorInline(admin.TabularInline):
    model = MovieActor
    extra = 1


class MovieDirectorInline(admin.TabularInline):
    model = MovieDirector
    extra = 1


class MovieProducerInline(admin.TabularInline):
    model = MovieProducer
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    search_fields = (
        'title',
        'release_year',
    )

    list_display = (
        "title",
        "release_year",
        "get_casting",
        "get_producers",
        "get_directors"
    )
    exclude = ['id']
    filter_horizontal = ["casting"]
    inlines = (MovieActorInline, MovieDirectorInline, MovieProducerInline)


admin.site.register(Movie, MovieAdmin)

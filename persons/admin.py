from django.contrib import admin
from persons.models import Person
from persons.models import Alias


class PersonAdmin(admin.ModelAdmin):
    search_fields = (
        'first_name',
        'last_name',
    )

    list_display = (
        "gender",
        "first_name",
        "last_name",
        "role",
        "get_aliases"
    )


class AliasAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        "name",
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Alias, AliasAdmin)

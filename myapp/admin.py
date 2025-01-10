from django.contrib import admin
from .models import Person,Team,MONTHS, SHIRT_SIZES

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'gender')
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name')
admin.site.register(Team)
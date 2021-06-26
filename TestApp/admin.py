from django.contrib import admin
from TestApp.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating','movielag']
admin.site.register(Movie,MovieAdmin)

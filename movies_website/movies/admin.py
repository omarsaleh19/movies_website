from django.contrib import admin
from .models import Movie
from django import forms
from .models import Review


admin.site.register(Movie)
admin.site.register(Review)


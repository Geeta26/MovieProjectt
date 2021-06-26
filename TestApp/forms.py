from django import forms
from TestApp.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'
from django import forms
from . models import Review, Movie

class AddMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title','slug','description','director','release_date','poster','actors']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }

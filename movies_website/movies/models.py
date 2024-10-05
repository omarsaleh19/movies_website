from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    director = models.CharField(max_length=100)
    release_date = models.DateField(help_text="YYYY-MM-DD")
    poster = models.ImageField(upload_to='posters/', blank=True)
    actors = models.TextField(help_text="Comma-separated list of main actors")
    
    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"

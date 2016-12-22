from django.db import models
from django.utils import timezone

class Language(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Pattern(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    language = models.ForeignKey('Language')
    code = models.TextField()
    history = models.TextField(null=True)
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    pattern = models.ForeignKey('Pattern')
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.author.name

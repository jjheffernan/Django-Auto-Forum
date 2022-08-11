from django.db import models


# Create your models here.

# - Project View App -
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="projects/static/img")

    def __str__(self):
        return self.title

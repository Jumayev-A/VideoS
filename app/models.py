from django.db import models

# Create your models here.
class Videos(models.Model):
    video = models.FileField(upload_to='videos/')
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
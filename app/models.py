from django.db import models
import uuid

# Create your models here.
class Videos(models.Model):
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    video = models.FileField(upload_to='videos/')
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
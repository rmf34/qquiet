from django.db import models
from .location import Location

class AudioFile(models.Model):
    db_table = ""
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    filename = models.TextField()
    file_size = models.IntegerField(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    class Meta:
        db_table = "audio_files"
        # app_label = "qquiet"

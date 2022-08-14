from django.db import models

# Create your models here.

class Location(models.Model):
    address = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    class Meta:
        db_table = "locations"
        # app_label = "qquiet"

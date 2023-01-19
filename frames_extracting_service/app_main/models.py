from django.db import models
from django_minio_backend import MinioBackend, iso_date_prefix

# Create your models here.
class Media(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=MinioBackend(bucket_name='media'),
                            upload_to=iso_date_prefix)
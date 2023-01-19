from django.db import models
from django_minio_backend import MinioBackend, iso_date_prefix

from .utils import get_frames_upload_to

# Create your models here.
class Media(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=MinioBackend(bucket_name='media'),
                            upload_to=iso_date_prefix)


class MediaFrames(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    uploaded_at = models.FileField(storage=MinioBackend(bucket_name='frames'),
                                    upload_to=get_frames_upload_to)
    
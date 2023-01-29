from django.db import models
from django_minio_backend import MinioBackend, iso_date_prefix

from .utils import get_frames_upload_to

# Create your models here.
class Media(models.Model):
    """Модель для хранения медиа файлов"""
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=MinioBackend(bucket_name='media'),
                            upload_to=iso_date_prefix)


class MediaFrames(models.Model):
    """Модель для хзранения кадров (в формате .zip)"""
    uploaded_at = models.DateTimeField(auto_now_add=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    frame = models.FileField(storage=MinioBackend(bucket_name='frames'),
                                    upload_to=get_frames_upload_to)
    
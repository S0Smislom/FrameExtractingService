# Generated by Django 4.1.5 on 2023-01-19 11:11

from django.db import migrations, models
import django.db.models.deletion
import django_minio_backend.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(storage=django_minio_backend.models.MinioBackend(bucket_name='media'), upload_to=django_minio_backend.models.iso_date_prefix),
        ),
        migrations.CreateModel(
            name='MediaFrames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.FileField(storage=django_minio_backend.models.MinioBackend(bucket_name='frames'), upload_to=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.media'))),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.media')),
            ],
        ),
    ]
from rest_framework import serializers
from .models import Media, MediaFrames


class MediaSerizlier(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class MediaFramesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFrames
        fields = ('media',)

class FrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFrames
        fields = '__all__'
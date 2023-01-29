from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Media, MediaFrames
from .serializers import MediaSerizlier, MediaFramesSerializer, FrameSerializer
from .services import frames_extracting_service



class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerizlier


class MediaFramesViewSet(ModelViewSet):
    queryset = MediaFrames.objects.all()
    serializer_class = FrameSerializer

    def get_serializer_class(self):        
        if self.action == "create":
            return MediaFramesSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer_data = MediaFramesSerializer(data=request.data)
        serializer_data.is_valid()
        validated_data = serializer_data.validated_data
        media = validated_data['media']
        fps = request.GET.get('fps', 1)
        result = frames_extracting_service.extract(media, fps)
        return Response(FrameSerializer(result, many=True).data)
    
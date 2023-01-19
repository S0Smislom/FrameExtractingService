import os
from . import path_service


def extract(media, media_temp_path):
    file_url = 'http://minio:9000/media/'+str(media.file)
    cmd = f'ffmpeg -i {file_url} -vf fps=1/1 {media_temp_path}/image_%04d.jpg'
    os.system(cmd)
    
def extract_frames(media, media_temp_path):
    extract(media, media_temp_path)
    images = path_service.listdir(media_temp_path)
    return [f"{media_temp_path}/{image}" for image in sorted(images)]

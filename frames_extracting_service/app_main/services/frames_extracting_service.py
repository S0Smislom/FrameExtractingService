from . import path_service, media_frames_service, ffmpeg_service


def extract(media):
    media_temp_path = path_service.get_or_create_clean_subpath(f'temp/{str(media.pk)}')
    media_frames_service.clear_db(media)
    images = ffmpeg_service.extract_frames(media, media_temp_path)
    uploaded = media_frames_service.upload_frames(images, media)
    path_service.remove_dir(media_temp_path)
    return uploaded
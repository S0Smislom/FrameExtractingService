from . import path_service, media_frames_service, ffmpeg_service


def extract(media, fps=1):
    media_temp_path = path_service.get_or_create_clean_subpath(f'temp/media/{str(media.pk)}')
    media_frames_service.clear_db(media)
    images = ffmpeg_service.extract_frames(media, media_temp_path, fps)
    archive_temp_path = path_service.get_or_create_clean_subpath(f'temp/archive')
    zip = media_frames_service.create_frames_zip(images, archive_temp_path, media)
    uploaded = media_frames_service.upload_frames([zip], media)
    path_service.remove_dir(media_temp_path)
    path_service.remove_dir(archive_temp_path)
    return uploaded
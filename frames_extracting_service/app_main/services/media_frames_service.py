from app_main.models import MediaFrames
import zipfile

def create_frame(media, file):
    frame = MediaFrames.objects.create(media=media)
    frame.frame.save(file.name.split('/')[-1], file, save=True)
    return frame

def create_frame_from_file(path, media):
    with open(path, 'rb') as file:
        created_frame = create_frame(media, file)
    return created_frame

def upload_frames(path_list, media):
    return [create_frame_from_file(path, media) for path in path_list]

def clear_db(media):
    MediaFrames.objects.filter(media = media).delete()

def create_frames_zip(path_list, archive_temp_path, media):
    zip_path = f'{archive_temp_path}/{media.pk}.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for path in path_list:
            zipf.write(path, path.split('/')[-1])
    return zip_path
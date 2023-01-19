from app_main.models import MediaFrames

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
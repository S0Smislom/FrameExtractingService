from pathlib import Path
import os
import shutil

from django.conf import settings


def get_base_path():
    return getattr(settings, 'BASE_DIR', Path(__file__).resolve().parent)

def get_or_create_path(path):
    """Возвращает или создает путь"""
    filepath = Path(path)
    filepath.mkdir(parents=True, exist_ok=True)
    return filepath

def clear_dir(path):
    for f in os.listdir(path):
        os.remove(path / f)

def remove_dir(path):
    shutil.rmtree(path)

def get_or_create_subpath(path):
    return get_or_create_path(get_base_path() / path)

def get_or_create_clean_subpath(path):
    path_ = get_or_create_subpath(path)
    clear_dir(path_)
    return path_

def listdir(path):
    return os.listdir(path)
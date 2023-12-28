# fileautomation/fileautomation.py

import os

downloads_path = "C:/Users/sgarn/Downloads"
# Images
img_terminations = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"]
# Audio
audio_terminations = ["mp3", "wav", "ogg", "flac", "aac"]
# Video
video_terminations = ["mp4", "avi", "mkv", "mov", "flv", "wmv"]
# Documents
document_terminations = ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "odt", "odp"]
# Archives
archive_terminations = ["zip", "rar", "7z", "tar", "gz"]
# Executable Files
executable_terminations = ["exe", "app", "sh"]
# Fonts
font_terminations = ["ttf", "otf"]
# Web Files
web_terminations = ["html", "css", "js", "json"]
# Database
database_terminations = ["sqlite", "db", "mdb"]
# Programming/Scripting
programming_terminations = ["py", "java", "cpp", "js", "php"]

all_terminations = (
    img_terminations +
    audio_terminations +
    video_terminations +
    document_terminations +
    archive_terminations +
    executable_terminations +
    font_terminations +
    web_terminations +
    database_terminations +
    programming_terminations
)
all_terminations_set = set(all_terminations)

def get_file_termination(file: str) -> str:
    file_lower = file.lower()
    for term in all_terminations_set:
        if file_lower.endswith(term) and os.path.isfile(f'{downloads_path}/{file}'):
            return term
    return ""

def handle_move(file: str, termination: str) -> None:
    handlers = {
        "img": img_terminations,
        "videos": video_terminations,
        "audio": audio_terminations,
        "documents": document_terminations,
        "archives": archive_terminations,
        "executables": executable_terminations,
        "fonts": font_terminations,
        "web_files": web_terminations,
        "database": database_terminations,
        "programming": programming_terminations,
    }

    for key, value in handlers.items():
        if termination in value:
            move(file, key)
            break

def move(file: str, dir_name: str) -> None:
    dir = f'{downloads_path}/{dir_name}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.rename(f'{downloads_path}/{file}', f'{dir}/{file}')


def main():
    download_files = os.listdir(downloads_path)
    for file in download_files:
        termination = get_file_termination(file)
        if termination:
            handle_move(file, termination)
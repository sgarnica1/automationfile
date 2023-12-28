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


def move(file: str, term: str) -> None:
    if handle_fonts(file):
        return 
    
    dir = f'{downloads_path}/{term}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.rename(f'{downloads_path}/{file}', f'{dir}/{file}')

def handle_fonts(file: str) -> bool:
    for term in font_terminations:
        if file.endswith(term):
            dir = f'{downloads_path}/fonts'
            if not os.path.exists(dir):
                os.makedirs(dir)
            os.rename(f'{downloads_path}/{file}', f'{dir}/{file}')
            return True
        
    return False

def handle_fonts(file: str) -> bool:
    for term in font_terminations:
        if file.endswith(term):
            dir = f'{downloads_path}/fonts'
            if not os.path.exists(dir):
                os.makedirs(dir)
            os.rename(f'{downloads_path}/{file}', f'{dir}/{file}')
            return True
        
    return False


def main():
    download_files = os.listdir(downloads_path)
    for file in download_files:
        for term in all_terminations:
            if file.endswith(term) and os.path.isfile(f'{downloads_path}/{file}'):
                move(file, term)
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


def move(file: str, dir: str) -> None:
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.rename(f'{downloads_path}/{file}', f'{dir}/{file}')

def handle_move(file: str, termination: str) -> None:
    if move_img(file):
        return
    
    if move_video(file):
        return
    
    if move_audio(file):
        return
    
    if move_documents(file):
        return
    
    if move_archives(file):
        return
    
    if move_executables(file):
        return
    
    if move_fonts(file):
        return
    
    if move_web_files(file):
        return
    
    if move_database(file):
        return
    
    if move_programming(file):
        return
    
    dir = f'{downloads_path}/{termination}'
    move(file, dir)
    

def handle_group_terminations(file: str, terminations: list, dir_name: str) -> bool:
    for term in terminations:
        if file.lower().endswith(term):
            dir = f'{downloads_path}/{dir_name}'
            move(file, dir)
            return True
    return False

def move_img(file: str) -> bool:
    dir_name = "img"
    return handle_group_terminations(file, img_terminations, dir_name)

def move_video(file: str) -> bool:
    dir_name = "videos"
    return handle_group_terminations(file, video_terminations, dir_name)

def move_audio(file: str) -> bool:
    dir_name = "audio"
    return handle_group_terminations(file, audio_terminations, dir_name)

def move_fonts(file: str) -> bool:
    dir_name = "fonts"
    return handle_group_terminations(file, font_terminations, dir_name)

def move_documents(file: str) -> bool:
    dir_name = "documents"
    return handle_group_terminations(file, document_terminations, dir_name)

def move_archives(file: str) -> bool:
    dir_name = "archives"
    return handle_group_terminations(file, archive_terminations, dir_name)

def move_executables(file: str) -> bool:
    dir_name = "executables"
    return handle_group_terminations(file, executable_terminations, dir_name)

def move_web_files(file: str) -> bool:
    dir_name = "web_files"
    return handle_group_terminations(file, web_terminations, dir_name)

def move_database(file: str) -> bool:
    dir_name = "database"
    return handle_group_terminations(file, database_terminations, dir_name)

def move_programming(file: str) -> bool:
    dir_name = "programming"
    return handle_group_terminations(file, programming_terminations, dir_name)


def main():
    download_files = os.listdir(downloads_path)
    for file in download_files:
        for term in all_terminations_set:
            file_lower = file.lower()   
            dir = f'{downloads_path}/{file}'
            if file_lower.endswith(term) and os.path.isfile(dir):
                handle_move(file, term)
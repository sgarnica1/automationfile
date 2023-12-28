# fileautomation/fileautomation.py

import os

# Define the path to the downloads folder
downloads_path = "C:/Users/sgarn/Downloads"

# Define lists of file terminations for different file types
img_terminations = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"]
audio_terminations = ["mp3", "wav", "ogg", "flac", "aac"]
video_terminations = ["mp4", "avi", "mkv", "mov", "flv", "wmv"]
document_terminations = ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "odt", "odp"]
archive_terminations = ["zip", "rar", "7z", "tar", "gz"]
executable_terminations = ["exe", "app", "sh"]
font_terminations = ["ttf", "otf"]
web_terminations = ["html", "css", "js", "json"]
database_terminations = ["sqlite", "db", "mdb"]
programming_terminations = ["py", "java", "cpp", "js", "php"]


# Combine all terminations into a set for efficient lookup
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
    """
    Determine the termination of a file based on its name and file existence.

    Args:
        file (str): The name of the file.

    Returns:
        str: The termination of the file.
    """
    file_lower = file.lower()
    for term in all_terminations_set:
        if file_lower.endswith(term) and os.path.isfile(f'{downloads_path}/{file}'):
            return term
    return ""

def handle_move(file: str, termination: str) -> None:
    """
    Move a file to its corresponding directory based on its termination.

    Args:
        file (str): The name of the file.
        termination (str): The termination of the file.
    """
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
    """
    Move a file to a specified directory.

    Args:
        file (str): The name of the file.
        dir_name (str): The name of the target directory.
    """
    dir = f'{downloads_path}/{dir_name}'
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.rename(f'{downloads_path}/{file}', f'{dir}/{file}')


def main():
    """
    Main function to organize files in the downloads folder based on their terminations.
    """
    download_files = os.listdir(downloads_path)
    for file in download_files:
        termination = get_file_termination(file)
        if termination:
            handle_move(file, termination)
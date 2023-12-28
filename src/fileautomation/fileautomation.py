# fileautomation/fileautomation.py

import os

downloads_path = "C:/Users/sgarn/Downloads"
exe_path = "C:/Users/sgarn/Downloads/exe"

file_terminations = ["png", "jpg", "mp4", "pdf", "zip", "exe" ]

def main():
    download_files = os.listdir(downloads_path)
    
    for file in download_files:
        for term in file_terminations:
            if file.endswith(term):
                dir = f'{downloads_path}/{term}'
                if not os.path.exists(dir):
                    os.makedirs(dir)
                os.rename(f'{downloads_path}/{file}', f'{dir}/{file}')
# fileautomation/fileautomation.py

import os

downloads_path = "C:/Users/sgarn/Downloads"
exe_path = "C:/Users/sgarn/Downloads/exe"

def main():
    download_files = os.listdir(downloads_path)

    for file in download_files:
        if file.endswith(".exe"):
            if not os.path.exists(exe_path):
                os.makedirs(exe_path)
            os.rename(f'{downloads_path}/{file}', f'{exe_path}/{file}')
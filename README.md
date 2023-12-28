# File Automation

File Automation is a Python script for organizing files in the downloads folder based on their terminations.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [File Terminations](#file-terminations)
- [License](#license)
- [Contributors](#contributors)

## Description

This script organizes files in the downloads folder by moving them to specific directories based on their file terminations. It supports various file types such as images, audio, video, documents, archives, executables, fonts, web files, databases, and programming/scripting files.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/sgarnica1/automationfile.git
   ```

2. Navigate to project directory

   ```bash
   cd automationfile
   ```

3. Install dependencies using pyproject.toml
    ```bash
    pip install -e .
    ```

4. Run the project with the .exe
    ```bash
    fileautomation.exe
    ```

    or run it as a Python module

    ```bash
    py -m fileautomation
    ```


## File Terminations

- **Images:** jpg, jpeg, png, gif, bmp, tiff, webp
- **Audio:** mp3, wav, ogg, flac, aac
- **Video:** mp4, avi, mkv, mov, flv, wmv
- **Documents:** pdf, doc, docx, xls, xlsx, ppt, pptx, odt, odp
- **Archives:** zip, rar, 7z, tar, gz
- **Executable Files:** exe, app, sh
- **Fonts:** ttf, otf
- **Web Files:** html, css, js, json
- **Database:** sqlite, db, mdb
- **Programming/Scripting:** py, java, cpp, js, php

## License

This project is licensed under the [MIT License](LICENSE).

## Contributors

- [Sergio Garnica González](mailto:sgarnica1902@gmail.com)

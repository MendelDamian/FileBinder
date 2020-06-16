import os
import shutil

# TODO categories management
categories = {'Documents': ['.doc', '.docx', '.txt', '.pdf'], 
              'Photos': ['.jpg', '.png', '.raw'], 
              'Archives': ['.zip', '.rar', '.tar'], 
              'Music': ['.mp3', '.flac'], 
              'Videos': ['.mp4'],
              'Applications': ['.exe']}


def move_files(files, path):
    if not path:
        raise ValueError('Path cannot be empty')
    if not files:
        return None

    for file in files:
        file_name = os.path.basename(file)
        name, ext = os.path.splitext(file_name)
        for (dir_, exts) in categories.items():
            # new_path = os.path.join(path, dir_, file_name)
            if ext in exts:
                new_path = os.path.join(path, dir_, file_name)
                shutil.move(file, new_path)
                print(f'File {file} moved to {os.path.join(dir_, file_name)}')
                break

            # print(f'File {file} moved to {os.path.join('Other', file_name)}')
            # shutil.move(file, os.path.join('Other', file))

import os
import shutil


def move_files(files, categories):
    '''Move files to their new directories.
    
    Args:
        files (LIST, TUPLE, SET): List of files to move
        categories (DICT): Categories
    '''
    # Check passed files
    if not files:
        return None

    for file in files:
        filename = os.path.basename(file)
        name, ext = os.path.splitext(filename)
        dirname = os.path.dirname(file)

        for (cat, exts) in categories[dirname].items():
            # Continue if exts if blank or ext is not in exts
            # IF EXTS IS NULL THEN EVERY EXTENSIONS FITS IN
            if ext not in exts or not exts:
                continue

            new_dir = os.path.join(dirname, cat)
            if not os.path.isdir(new_dir):
                os.makedirs(new_dir)

            new_path = os.path.join(new_dir, filename)
            shutil.move(file, new_path)
            print(f'File {file} moved to {os.path.join(new_path)}')
            break

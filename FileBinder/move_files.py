import os
import shutil


def move_files(files, path, categories):
    '''Move files to their new directories.
    
    Args:
        files (LIST, TUPLE, SET): List of files to move
        path (TYPE): The path from which they will be moved
        categories (DICT): Categories
    
    Raises:
        ValueError: Path cannot be empty
    '''
    # Check passed path
    if not path:
        raise ValueError('Path cannot be empty')
    # Check passed files
    if not files:
        return None

    for file in files:
        file_name = os.path.basename(file)
        name, ext = os.path.splitext(file_name)
        moved = False
        for (dir_, exts) in categories.items():
            if ext in exts:
                new_path = os.path.join(path, dir_, file_name)
                shutil.move(file, new_path)
                print(f'File {file} moved to {os.path.join(dir_, file_name)}')
                moved = True
                break
        # If files were not moved, they will go to Other/
        if not moved:
            new_path = os.path.join(path, 'Other', file_name)
            print(f'File {file} moved to {new_path}')
            shutil.move(file, new_path)

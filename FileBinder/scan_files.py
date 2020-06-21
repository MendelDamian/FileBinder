from FileBinder.SkipFiles import SkipFiles
import os


def scan_files(categories):
    '''Scan for new files other then in skip file and categories
    
    Args:
        categories (DICT): Categories object
    
    Returns:
        SET: New files
    '''
    skip = SkipFiles().get()
    files = set()

    for (_dir, cats) in categories.items():
        skip_cat = set(cats.keys())

        for file in os.listdir(_dir):
            scanned_files = set([file]).difference(skip)
            scanned_files = scanned_files.difference(skip_cat)
            if scanned_files:
                files.add(os.path.join(_dir, file))

    return files

from FileBinder.SkipFiles import SkipFiles
import os


def scan_files(path, categories):
    '''Scan for new files other then in skip file and categories
    
    Args:
        path (TYPE): path to be scanned
        categories (DICT): List of categories
    
    Returns:
        SET: New files
    '''
    skip = SkipFiles().get()
    files = set()
    for file in os.listdir(path):
        if set([file]).difference(skip).difference(set(categories.keys())):
            files.add(os.path.join(path, file))
    return files

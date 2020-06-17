from time import sleep
from FileBinder.scan_files import scan_files
from FileBinder.move_files import move_files


def listen(path, categories, tick=5):
    """Listen to file changes in specific directory
    
    Args:
        path (TYPE): Path to listen
        categories (DICT): List of categories
        tick (int, optional): Value of delay after each check
    """
    while True:
        files = scan_files(path, categories)
        if files:
            move_files(files, path, categories)

        sleep(tick)

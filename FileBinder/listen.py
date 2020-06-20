from time import sleep
from FileBinder.scan_files import scan_files
from FileBinder.move_files import move_files


def listen(categories, tick=5):
    """Listen to file changes in specific directory
    
    Args:
        categories (DICT): List of categories
        tick (int, optional): Value of delay after each check
    """
    while True:
        files = scan_files(categories)
        if files:
            try:
                move_files(files, categories)
            except PermissionError:
                pass

        sleep(tick)

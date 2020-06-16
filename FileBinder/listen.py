from time import sleep
from FileBinder.scan_files import scan_files
from FileBinder.move_files import move_files

# TODO

def listen(path, tick=5):
    """Summary
    
    Args:
        path (TYPE): Description
        tick (int, optional): Description
    """
    while True:
        files = scan_files(path)
        if files:
            move_files(files, path)

        sleep(tick)

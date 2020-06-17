import os


def get_desktop_path():
    '''Get desktop path
    
    Returns:
        TYPE: User's desktop path
    '''
    return os.path.expanduser('~/Desktop')

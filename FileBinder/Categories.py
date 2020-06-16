import os

# TODO categories management
categories = {'Documents': ['.doc', '.docx', '.txt', '.pdf'], 
              'Photos': ['.jpg', '.png', '.raw'], 
              'Archives': ['.zip', '.rar', '.tar'], 
              'Music': ['.mp3', '.flac'], 
              'Videos': ['.mp4'],
              'Applications': ['.exe'],
              'Other': []}


class Categories:
    def __init__(self, path):
        self._path = path

    def create_dirs(self):
        '''Create directories for categories.'''
        for cat in categories.keys():
            path = os.path.join(self._path, cat)
            if not os.path.isdir(path):
                os.makedirs(path)
                print(f'Creating new directory: {path}')

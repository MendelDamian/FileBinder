import os
import json
from FileBinder.get_download_path import get_download_path


class Categories:
    def __init__(self):
        '''Categories manager
        '''
        self._filename = 'categories.json'
        self.create_file()
        self.read()
        self.create_dirs()

    def create_file(self):
        '''Creates json file and fills it with default values.
        '''
        if not os.path.isfile(self._filename):
            self.write(self.get_defaults())

    def add(self, categories):
        '''Add new categories

        Format:
            {PATH_TO_LISTEN: 
                {CATEGORY: ['.extensions']}
            }
        
        Args:
            categories (DICT): New categories
        '''
        #TODO Syntax checker
        self._categories.update(categories)
        self.wirte(self._categories)

    def read(self):
        '''Read json file with categories setup.
        '''
        with open(self._filename, 'r') as f:
            self._categories = json.load(f)

    def write(self, content):
        '''Write categories to json.
        
        Args:
            content (DICT): Categories
        '''
        with open(self._filename, 'w') as f:
            json.dump(content, f)

    def get(self):
        '''Get categories.
        
        Returns:
            DICT: Categories
        '''
        return self._categories

    def create_dirs(self):
        '''Create directories for categories.
        '''

        for (dir_, cats) in self._categories.items():
            for cat in cats.keys():
                dirpath = os.path.join(dir_, cat)
                if not os.path.isdir(dirpath):
                    os.makedirs(dirpath)
                    print(f'Creating new directory: {dirpath}')

    def get_defaults(self):
        '''Get default values for categories.
        
        Returns:
            DICT: Default categories
        '''
        download_path = get_download_path()
        return {
            download_path: {
                'Documents': ['.doc', '.docx', '.txt', '.pdf'], 
                'Photos': ['.jpg', '.png', '.raw'], 
                'Archives': ['.zip', '.rar', '.tar'], 
                'Music': ['.mp3', '.flac'], 
                'Videos': ['.mp4'],
                'Applications': ['.exe'],
                'Other': []
            }
        }

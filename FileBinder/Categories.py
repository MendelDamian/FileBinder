import os
import json


class Categories:
    def __init__(self):
        '''Categories manager
        '''
        self._filename = 'categories.json'
        self.create_file()
        self.read()

    def create_file(self):
        '''Creates json file and fills it with default values.
        '''
        if not os.path.isfile(self._filename):
            self.write(self.get_defaults())

    def add(self, categories):
        '''Add new categories
        
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

    def create_dirs(self, path):
        '''Create directories for categories.
        '''
        for cat in self._categories.keys():
            fpath = os.path.join(path, cat)
            if not os.path.isdir(fpath):
                os.makedirs(fpath)
                print(f'Creating new directory: {fpath}')

        # Hard coded one directory
        if not os.path.isdir(os.path.join(path, 'Other')):
            os.makedirs('Other')
            print(f'Creating new directory: Other')

    # def edit_filename(self, new_filename):
    #     '''Edit filename of categories.
        
    #     args:
    #         new_filename: Name of new file
    #     '''
    #     # Check if filename is not empty.
    #     if not new_filename:
    #         raise ValueError('Filename cannot be empty.')

    #     # Check if filename has .json extension.
    #     ext = '.json'
    #     if new_filename[-4:] != ext:
    #         new_filename = f'{new_filename}{ext}'

    #     os.rename(self._filename, new_filename)
    #     self._filename = new_filename

    def get_defaults(self):
        '''Get default values for categories.
        
        Returns:
            DICT: Default categories
        '''
        return {
            'Documents': ['.doc', '.docx', '.txt', '.pdf'], 
            'Photos': ['.jpg', '.png', '.raw'], 
            'Archives': ['.zip', '.rar', '.tar'], 
            'Music': ['.mp3', '.flac'], 
            'Videos': ['.mp4'],
            'Applications': ['.exe']
        }

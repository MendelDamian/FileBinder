import os
from FileBinder.get_download_path import get_download_path


class SkipFiles:
    def __init__(self):
        '''Skipping files while scanning.
        '''
        self._files = set()
        self._filename = 'skip.json'
        self.create_file()
        self.read()

    def create_file(self):
        '''Creates file with defaults settings if doesn't exist.
        '''
        if not os.path.isfile(self._filename):
            self._files = self.get_defaults()
            self.write()

    def read(self):
        '''Read file where are all files to skip.

        File example:
        desktop.ini
        Important.zip
        '''
        with open(self._filename, 'r') as f:
            for item in f:
                self._files.add(item)

    def add(self, fnames):
        '''Add new file to list.
        
        Args:
            filename (LIST SET TUPLE): paths of new exluded files.
        '''
        self._files.update(fnames)
        self.write()

    def get(self):
        '''Return list of excluded files.
        '''
        return self._files

    def write(self):
        '''Write to a file
        '''
        with open(self._filename, 'w') as f:
            for item in self._files:
                f.write(f'{item}\n')

    def remove(self, excluded):
        '''Remove specific registration from set and file.

        args:
            excluded (LIST SET TUPLE): Path of exluded file or directory
        '''
        self._files.difference(excluded)
        self.write()

    def clear(self):
        '''Clear list of excluded files.
        '''
        open(self._filename, 'w').close()
        self._files.clear()

    def empty(self):
        '''Return if list of exluded files is empty.'''
        return True if len(self._files) == 0 else False

    def length(self):
        '''Return length of exclusion list.
        '''
        return len(self._files)

    def get_defaults(self):
        '''Get defualt values.

        Returns:
            SET: Default skip file values
        '''
        download_path = get_download_path()
        return {os.path.join(download_path, 'desktop.ini'), os.path.join(download_path, 'important.zip')}


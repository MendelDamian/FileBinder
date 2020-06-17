import os


class SkipFiles:
    def __init__(self):
        '''Skipping files while scanning.
        '''
        self._files = set()
        self._filename = 'skip.txt'
        self.create_file()
        self.read()

    def create_file(self):
        '''Creates file with defaults settings if doesn't exist.
        '''
        if not os.path.isfile(self._filename):
            with open(self._filename, 'w') as f:
                for el in self._files:
                    f.write(f'{el}\n')

    def read(self):
        '''Read file where are all files to skip.

        File example:
        desktop.ini
        Important.zip
        '''
        with open(self._filename, 'r') as f:
            lines = f.read().splitlines()
            lines = [l.strip() for l in lines if l]
            self._files.update(lines)

    def add(self, filename):
        '''Add new file to list.
        
        Args:
            filename (String): name of new exluded files.
        
        Returns:
            None: If all passed files were already in list.
        
        Raises:
            ValueError: Filename cannot be empty.
        '''
        if type(filename) in [tuple, list, set]:
            filename = [fn.strip() for fn in filename if fn and fn not in self._files]
            # If empty = all passed files were already in list.
            if not filename:
                return None
        else:
            filename = filename.strip()

        # Check if filename is not empty.
        if not filename:
            raise ValueError('Filename cannot be empty.')

        self._files.update(filename)
        with open(self._filename, 'a') as f:
            for fn in filename:
                f.write(f'{fn}\n')

    def get(self):
        '''Return list of excluded files.
        '''
        return self._files

    # def edit_filename(self, new_filename):
    #     '''Edit filename of exclusion list.
        
    #     args:
    #         new_filename: Name of new file
    #     '''
    #     # Check if filename is not empty.
    #     if not new_filename:
    #         raise ValueError('Filename cannot be empty.')

    #     # Check if filename has .txt extension.
    #     if new_filename[-4:] != '.txt':
    #         new_filename = f'{new_filename}.txt'

    #     os.rename(self._filename, new_filename)
    #     self._filename = new_filename

    def remove(self, excluded):
        '''Remove specific registration from set and file.

        args:
            excluded: Name of exluded file or directory
        '''
        if type(excluded) in [tuple, list, set]:
            excluded = [ex.strip() for ex in excluded if ex]
        else:
            excluded = excluded.strip()

        if not excluded:
            raise ValueError('Filename cannot be empty.')

        # From self._files.
        for ex in excluded:
            self._filename.discard(ex)

        # From 'skip.txt' or other file if ealier changed.
        with open(self._filename, 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                line = line.strip()
                if line and line not in excluded:
                    f.write(f'{line}\n')

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
        return {'desktop.ini'}


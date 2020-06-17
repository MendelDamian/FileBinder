#!/usr/bin/python3
from FileBinder.listen import listen
from FileBinder.get_download_path import get_download_path
from FileBinder.Categories import Categories
import sys

# TODO Bind other directories
# TODO GUI
def main():
    path = get_download_path()
    cats = Categories()
    cats.create_dirs(path)
    listen(path, cats.get())


if __name__ == '__main__':
    main()

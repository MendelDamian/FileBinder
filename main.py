from FileBinder.listen import listen
from FileBinder.get_download_path import get_download_path
from FileBinder.Categories import Categories

# TODO Categories manager
# TODO Bind other directories
# TODO Every other file move to other

def main():
    path = get_download_path()
    Categories(path).create_dirs()
    listen(path)


if __name__ == '__main__':
    main()

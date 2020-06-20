#!/usr/bin/python3
from FileBinder.listen import listen
from FileBinder.Categories import Categories
import sys


def main():
    cats = Categories()
    listen(cats.get())


if __name__ == '__main__':
    main()

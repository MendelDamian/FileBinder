from FileBinder.Categories import Categories
from FileBinder.SkipFiles import SkipFiles
import os
import sys


choices = {
            '1': cats,
            '2': skip,
            '3': exit
           }


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def logo():
    print('''
        #########################################
        #                                       #
        #         F I L E   B I N D E R         #
        #                                       #
        #########################################
    ''')


def main_menu():
    cls()
    logo()
    print('''
        1) Manage Categories
        2) Manage Files to Skip

        3) Exit

         >> ''', end='')

    choice = input()
    return choice


def exit():
    sys.exit(0)


def skip():
    s = SkipFiles()
    skips = s.get()

    for i, item in enumerate(skips):
        print(f'{i}) item')


def cats():
    cat = Categories()


def loop():
    while True:
        choice = main_menu()
        # Valid choice
        if choice not in choices.keys():
            continue

        cls()
        choices[choice]()


if __name__ == '__main__':
    loop()

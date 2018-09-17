# file: get_rand.py
from random import choice
from time import sleep


def main():
    print(choice('abcdefghijklmnopqrstuvwxyz'))
    sleep(2)


if __name__ == '__main__':
    main()

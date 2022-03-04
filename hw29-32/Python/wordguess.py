#!/usr/bin/env python3

import sys

from myinput import get_data

def to_check(words: list):
    try:
        all(isinstance(x, str) for x in words)
    except:
        print("Not all values are strings! Please check the sequence.")
        exit(0)
    else:
        return words

def to_guess(data: list):
    words = to_check(data)
    fw_flag = False
    try:
        import fuzzywuzzy
    except ImportError as e:
        pass
    else:
        fw_flag = True
    while True:
        word = input("Please enter any word:")
        if word in words:
            print("You guess the word!")
            sys.exit(0)
        else:
            print("You miss! Try again!")
        if fw_flag:
            print("Let`s see how close your guess to other words in the list: ")
            print(fuzz_ratio(word, item) for item in words)

if __name__ == "__main__":
    data = get_data()
    if data[0].startswith("["):
        data[0] = data[0][1:]
        data[-1] = data[-1][:-1]
    to_guess(data)
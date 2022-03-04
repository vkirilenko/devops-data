#!/usr/bin/env python3

import sys

from myinput import get_data, to_check

def to_print(data: list):
    numbers = to_check(data)
    for num in numbers:
        if num == 254:
            print(num)
            sys.exit(0)
        else:
            if num%2 == 0:
                print(num)

if __name__ == "__main__":
    data = get_data()
    if data[0].startswith("["):
        data[0] = data[0][1:]
        data[-1] = data[-1][:-1]
    to_print(data)

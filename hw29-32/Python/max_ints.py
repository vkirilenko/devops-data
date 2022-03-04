#!/usr/bin/env python3

import os

from myinput import get_data

def to_check(numbers: list):
    try:
        numbers = list( map(int, numbers) )
    except:
        error_elements = []
        for item in numbers:
            try:
                int(item)
            except:
                error_elements.append(item)
        print(f"You've passed some extra elements that I can't parse: {error_elements}")
        return list( map(int, [num for num in numbers if num not in error_elements]) )
    else:
        return numbers

def max_find(data: list):
    numbers = to_check(data)
    return(sorted(numbers, reverse = True)[:3])

if __name__ == "__main__":
    data = get_data()
    if data[0].startswith("["):
        data[0] = data[0][1:]
        data[-1] = data[-1][:-1]
    max_find(data)
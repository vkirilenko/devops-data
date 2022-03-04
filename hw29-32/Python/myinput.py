#!/usr/bin/env python3
import sys

def get_data():
    arg_lst = sys.argv[1:]
    if len(arg_lst) == 0:
        print("You need to enter at least one argument!")
        sys.exit(1)
        return ""
    if len(arg_lst) > 1:
        arg_lst = ''.join(arg_lst)
        arg_lst = arg_lst.split(",")
    return arg_lst

def to_check(numbers: list):
    try:
        numbers = list( map(int, numbers) )
    except:
        print("Not all values are numbers! Please, check the sequence.")
        exit(0)
    else:
        return numbers

def to_print(data: list):
    numbers = to_check(data)
    print(numbers)
    print(tuple(numbers))

if __name__ == "__main__":
    data = get_data()
    to_print(data)

#!/usr/bin/env python3

import os

from myinput import get_data

def to_dict(data: list):
    output = dict()
    for item in list(data[0]):
        output[item] = output.get(item, 0) +1
    #for symbol, count in output.items():
    #    print(f"Symbol {symbol} met {count} times")
    return output

if __name__ == "__main__":
    data = get_data()
    to_dict(data)
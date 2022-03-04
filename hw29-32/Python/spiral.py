#!/usr/bin/env python3

import os

from myinput import get_data, to_check

def calculate(size: int):
    table = [[0] * size for i in range(size)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(size + size - 1):
        for j in range((size + size - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            table[x][y] = c
            c += 1
    return table

def print_spiral(data: list):
    size = to_check(data)[0]
    for line in calculate(size):
        print(' '.join(str(num).zfill(2) for num in line))

if __name__ == "__main__":
    data = get_data()
    print_spiral(data)

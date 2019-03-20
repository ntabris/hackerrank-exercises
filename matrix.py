#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)


    unwound = ''.join([ line[char] for char in range(m) for line in matrix  ])

    clean = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])',' ',unwound)
    print(clean)

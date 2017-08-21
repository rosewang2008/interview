#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    sum = 0
    for number in ar:
        sum += number
    return sum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
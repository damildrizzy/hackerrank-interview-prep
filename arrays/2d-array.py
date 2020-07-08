#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    n = 0
    while n < 4:
        for idx, ar in enumerate(arr[n][:-2]):
            first_row = sum(arr[n][idx:idx+3])
            second_row = arr[n+1][idx+1]
            third_row = sum(arr[n+2][idx:idx+3])
            total_sum = first_row + second_row + third_row
            sums.append(total_sum)
        n+=1
    return max(sums)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


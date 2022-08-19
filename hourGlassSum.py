#!/bin/python3

import math
import os
import random
import re
import sys

#
#
# Function Description

'''Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

int arr[6][6]: an array of integers

Returns
int: the maximum hourglass sum
'''

def hourglassSum(arr):
    return max([arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1] for i in range(1, len(arr)-1) for j in range(1, len(arr)-1)]) 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

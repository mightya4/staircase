#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    empty_space = n - 1
    num_of_stair = 1
    for i in range(0, n):
        stair = ""
        if num_of_stair <= n:
            stair = (" " * empty_space) + (num_of_stair * "#")
            empty_space -= 1
            num_of_stair += 1
        print(stair)
        
        
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

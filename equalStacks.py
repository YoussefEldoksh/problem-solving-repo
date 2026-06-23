#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):

    
    
    sum1,sum2,sum3 = sum(h1),sum(h2),sum(h3)
    element = 0

    while sum1 != sum2 or sum1 != sum3 or sum2 != sum3:
        maximum = max(sum1,sum2,sum3)
        if maximum == sum1:
            element = h1.pop(0)
            sum1 -= element
        if maximum == sum2:
            element = h2.pop(0)
            sum2 -= element
        if maximum == sum3:
            element = h3.pop(0)
            sum3 -= element
    return sum1
    
    
    
     
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

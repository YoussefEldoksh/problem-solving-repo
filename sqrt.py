import math

def mySqrt(x):
    if x == 0: return 0
    if x == 1: return 1
    i = x/2
    while i > 0:
        if (i/2)*(i/2) > x: 
            i = (i/2)+1
        if i*i <= x:
            return i
        else : i-=1


print(mySqrt(2))
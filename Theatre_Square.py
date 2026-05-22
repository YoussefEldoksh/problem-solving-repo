import math

def number_of_stones(n,m,a):
    if n == 0 or m == 0 or a == 0:
        return 0 
    rows = math.ceil(n/a)
    cols = math.ceil(m/a)

    return rows*cols



n,m,a = map(int,input().split(" "))

print(number_of_stones(n,m,a))

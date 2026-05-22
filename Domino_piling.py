
def max_dominos(m,n):
    result = (m*n) // 2
    return result
m,n = map(int,list(input().split(" ")))

print(max_dominos(m,n))

def power(x,n):
    if n == 0 :
        return 1
    res = power(x,n//2)
    if n % 2 == 0:
        return res*res
    if n % 2 != 0:
        return res*res*x
    
print(power(2,3))
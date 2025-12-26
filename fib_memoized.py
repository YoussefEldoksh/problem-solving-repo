
def fib(n,memo):
    if n == 0 or n == 1: 
        return n
    if(not memo[n]):
        memo[n] = fib(n-2,memo) + fib(n-1,memo)
    return memo[n]


memo = [0] * 6
fib(5,memo)
print(memo)
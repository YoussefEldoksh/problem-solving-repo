
def stair_case(n,memo):
    if n <= 0:
        return 0
    if n == 2 or n == 3:
        return 1
    if(not memo[n]):
        memo[n] =  stair_case(n-2,memo) + stair_case(n-3,memo) 
    return memo[n]
        

n = 7
memo = [0] * (n+1)
print(stair_case(n,memo))
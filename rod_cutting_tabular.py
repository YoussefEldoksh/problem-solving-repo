

def rod_cutting(prices):
    n = len(prices) - 1  # max rod length
    revenue = [0] * (n + 1)
    solutions = [0] * (n+1)
    for i in range(1,len(prices)):
        max_rev = float('-inf')
        for j in range(1,i+1):
            if max_rev < prices[j] + revenue[i-j]:
                max_rev = prices[j]+revenue[i-j]
                solutions[i] = j
        revenue[i] = max_rev
    i = 1
    while(n > 0):
        print(f' piece number {i}: ',solutions[n])
        n = n - solutions[n]
        i += 1
    return revenue,solutions  
    
prices = [0,1,5,8,9,10,17,17,20]

print(rod_cutting(prices))
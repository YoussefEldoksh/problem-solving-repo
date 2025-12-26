

def coinChange(coins,amount):
    if amount == 0:
        return 0
    nums = [-1] * (amount+1)
    nums [0] = 0

    for i in range(1,amount+1):
        nums[i] = float('inf')
        for j in range(0,len(coins)):
            if coins[j] <= i:
                nums[i] = min(nums[i], 1 + nums[i - coins[j]])
    return nums[amount] if nums[amount] != float('inf') else -1


    

coins = [1,2,5]
amount = 11

print(coinChange(coins,amount))

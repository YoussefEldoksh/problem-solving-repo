def productExceptSelf(nums):
    
    prefix = []
    postfix = []
    answer = []
    for i in range(len(nums)):
        if i-1 < 0:
            prefix.append(1*nums[i])
        else:
            prefix.append(prefix[i-1]*nums[i])
    j = 0
    for i in range(len(nums)-1,-1,-1):
        if i+1 > len(nums)-1:
            postfix.append(1*nums[i])
        else:
            postfix.append(postfix[j-1]*nums[i])
        j+=1
    postfix.reverse()   
    print(prefix)
    print(postfix)
    print(answer)
    for i in range(len(nums)):
        if i-1 < 0:
            answer.append(1*postfix[i+1])
            print(f"iteration {i}: 1*{postfix[i-1]}")

        elif i+1 == len(nums):
            answer.append(1*prefix[i-1])
            print(f"iteration {i}: {prefix[i-1]}*1")

        else:
            answer.append(prefix[i-1]*postfix[i+1])
            print(f"iteration {i}: {prefix[i-1]}*{postfix[i-1]}")
    return answer


print(productExceptSelf([1,2,3,4]))
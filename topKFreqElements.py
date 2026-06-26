

def topKFrequent(nums, k: int):
    hashset = dict.fromkeys(nums,0)
    result = []
    for i in nums:
        hashset[i] += 1
    
    for i in range(k):
        maximum = max(hashset,key=hashset.get)
        result.append(maximum)
        hashset.pop(maximum)
        
    return result


arr = [1,2,1,2,1,2,3,1,3,2]

print(topKFrequent(arr,2))
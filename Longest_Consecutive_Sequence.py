def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
        
    hashset = set(nums)
    longest = 0
    for i in hashset:
        if i-1 not in hashset:
            length = 0
            while i+length in hashset:
                length +=1
            if length >= longest:
                longest = length
            
    return longest


arr = [1,100]

print(longestConsecutive(arr))
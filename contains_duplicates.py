

def has_dups(nums):
    hashmap = set()
    for i in nums:
        if i in hashmap:
            return True
        hashmap.add(i)
    print(hashmap)
    return False



nums = [7,4,2,6,8,14]

print(has_dups(nums))
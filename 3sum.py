

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    print(nums)
    result_arr = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        low = i+1
        high = len(nums)-1
        while low < high:
            result = nums[i] + nums[low] + nums[high]
            if result > 0:
                high -= 1
            elif result < 0:
                low += 1
            else:
                result_arr.append([nums[i],nums[low],nums[high]])
                low += 1
                while nums[low] == nums[low-1] and low < high:
                    low += 1

    return result_arr
            

arr = [1,2,0,1,0,0,0,0]


res = threeSum(arr)
print(res)


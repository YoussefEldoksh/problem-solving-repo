
from typing import List
from max_in_rotated_arr import maximum


def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    maximum = max(nums)
    myArr = list(range(0, maximum+1))
    print(myArr)
    summation = sum(myArr) - sum(nums) 
    if summation == 0 and min(nums) == 0:
        return maximum+1
    if summation == 0 and min(nums) > 0:
        return 0
    return summation

arr = [9,6,4,2,3,5,7,0,1]

print(missingNumber(arr))
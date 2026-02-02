from typing import List
from contains_duplicates import nums


def removeDuplicates(nums: List[int]) -> int:
    first = 0

    for last in range(1,len(nums)):
        if nums[first] < nums[last]:
            first += 1
            nums[first] = nums[last]
    print(nums)

arr = [-1,0,0,0,0,3,3]

removeDuplicates(arr)
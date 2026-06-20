def rotate(nums: List[int], k: int) -> None:
    nums[:] = nums[::-1]
    k %= len(nums)
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]  
    
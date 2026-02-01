def searchInsertRec(nums,target,low,high):
    if low > high:
        return low
    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return searchInsertRec(nums,target,mid+1,high)
    else:
        return searchInsertRec(nums,target,low,mid-1)
    

arr = [1,3,5,6]
print(searchInsertRec(arr,5,0,len(arr)-1))

def searchRange(nums, target):
    i = 0
    j = len(nums)-1
    if len(nums) == 1:
        if nums[0] == target:
            return [0,0]
        else:
            return [-1,-1]
    while i <= j:
        if nums[i] != target:
            i+=1
        if nums[j] != target:
            j-=1
        if nums[i] == target and nums[j] == target:
            return [i,j]
    return [-1,-1]

# the above solution is way better

# def binarySearch(nums,target):
#     high = len(nums)-1
#     low = 0

#     while(low < high):
#         mid = (low+high) // 2
#         if nums[mid] == target:
#             return mid
#         if nums[mid] > target:
#             high = mid-1
#         if nums[mid] < target:
#             low = mid+1
#     return -1
        
# def searchRange(nums, target):

#     if len(nums) == 1:
#         if nums[0] == target:
#             return [0,0]
#         else:
#             return [-1,-1]
#     targetIndex = binarySearch(nums,target)

#     if targetIndex == -1:
#         return [-1,-1]
#     i = targetIndex
#     j = targetIndex
#     while i > 0 and nums[i - 1] == target:
#         i -= 1
#     while j < len(nums) - 1 and nums[j + 1] == target:
#         j += 1
#     return [i,j]

print(searchRange([1,4], 4))


def binary_search(arr,low,high,target):
    mid = (low+high) // 2
    if low > high:
        return False
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr,mid+1,high,target)
    else:
        return binary_search(arr,low,mid-1,target)
    

arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

result = binary_search(arr,0,len(arr)-1,9)

print(result)
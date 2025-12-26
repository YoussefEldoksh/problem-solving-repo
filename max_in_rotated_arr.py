
def maximum(a,low,high):
    if low == high:
        return a[low]
    mid = (low+high)//2
    if a[mid] > a[mid+1]:
        return a[mid]
    if a[mid] < a[low]:
        return maximum(a,low,mid-1)
    if a[mid] > a[low]:
        return maximum(a,mid+1,high)
    
arr = [35,42,5,15,27,29]

print(maximum(arr,0,len(arr)-1))
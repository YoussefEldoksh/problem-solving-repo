def partition(low,high,arr):
    pivot = arr[high]
    i = low-1
    
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return i+1
    

def findMedian(arr):
    mid = (len(arr)-1)//2
    
    def quicksort(low,high,arr):
        if low < high:
            pivot = partition(low,high,arr)
            if pivot == mid:
                return arr[pivot]
        return quicksort(low, pivot-1, arr) or quicksort(pivot+1, high, arr)
    return quicksort(0,len(arr)-1,arr)


arr = {}
print(findMedian(arr))
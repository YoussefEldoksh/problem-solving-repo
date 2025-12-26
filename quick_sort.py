

def partition(A,low,high):
    pivot = A[high]
    i = low-1
    for j in range(low,high):
        if A[j] < pivot:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[high],A[i+1] = A[i+1],A[high]
    print(A)
    return i + 1

def quick_sort(A,low,high):
    if low < high:
        pivot = partition(A,low,high)
        quick_sort(A,low,pivot-1)
        quick_sort(A,pivot+1, high)
    return A


arr = [10,80,90,60,30,20]

print(quick_sort(arr,0,len(arr)-1))
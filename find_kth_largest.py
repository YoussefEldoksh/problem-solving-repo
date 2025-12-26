
def partition(A,low,high):
    pivot = A[high]
    i = low-1
    for j in range(low,high):
        if A[j] > pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[high],A[i+1] = A[i+1],A[high]
    print(A)
    return i + 1

def find_kth(A,low,high,k):
    if low == high:
        return low
    pivot = partition(A,low,high)
    rank = pivot - low + 1
    if rank == k:
        return pivot
    if rank > k:
        return find_kth(A,low,pivot-1,k)
    if rank < k:
        return find_kth(A,pivot+1,high,k-rank) #we subtract the rank because since the k is greated than the rank of the
                                               #pivot we recived by some number so that number must be the rank of the needed
                                               #element in the new array (right part)


arr = [3,2,3,1,2,4,5,5,6]

index = find_kth(arr,0,len(arr)-1,4)
print(arr[index])
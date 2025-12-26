import random

def partition(A,low,high):
    pivot = random.randint(low,high)
    i = low-1
    for j in range(low,high):
        if A[j] > pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[high],A[i+1] = A[i+1],A[high]
    print(A)
    return i + 1


def largest_k_elements(A,low,high,k):
    if low == high:
        return low




def count_sort(A,num_range):
    counting_arr = [0]*(num_range+1)
    result = [0]*len(A)
    

    for i in range(0,len(A)):
        counting_arr[A[i]] = counting_arr[A[i]] + 1

    # for i in range(0,len(A)):
    #     for j in range(0,counting_arr[i]):
    #         print(i)

    for i in range(1,num_range+1):  #this makes it stable -> elements of the same value appear in the same order as before 
        counting_arr[i] += counting_arr[i-1]    

    for i in range(len(A)-1,-1,-1):
        result[counting_arr[A[i]]-1] = A[i]
        counting_arr[A[i]] -= 1
    return result


arr = [0, 3, 3, 0, 1, 1, 0, 1]

print(count_sort(arr,3))


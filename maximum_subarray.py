


def max_crossing(A,low,mid,high):
    left_sum = -10000
    sum = 0
    max_left = mid

    for i in range (mid,low-1,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    sum = 0
    right_sum = -10000
    max_right = mid+1

    for i in range(mid+1,high+1):
        sum = sum + A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left,max_right, (left_sum+right_sum)  if (left_sum + right_sum) > 0 else left_sum if left_sum > right_sum else right_sum

def max_subarray(arr,low,high):
    if low == high:
        return low,high,arr[low]
    else:
        print("Dividing:", arr[low:high+1])
        mid = (low+high)//2
        left_start,left_end,left_sum = max_subarray(arr,low,mid)
        right_start,right_end,right_sum = max_subarray(arr,mid+1,high)
        crossing_start,crossing_end,crossing_sum = max_crossing(arr,low,mid,high)

        print("Conquering:", arr[low:high+1])


        if left_sum >= right_sum and left_sum >= crossing_sum:
            return left_start,left_end,left_sum
        elif right_sum >= left_sum and right_sum >= crossing_sum:
            return right_start,right_end,right_sum
        else:
            return crossing_start,crossing_end,crossing_sum


arr = [-1,-6,-9,4,-8,5,-4,2,-1,1,-8,0,1,3,1]

start,end,sum = max_subarray(arr,0,len(arr)-1)

print("Subarray:", arr[start:end+1])

print("Sum:", sum)
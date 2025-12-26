
def reverseBits(n):
    bits = list(map(int, format(n, '032b')))
    print(bits)
    auxreverseBits(bits,0,len(bits)-1)
    print(bits)
    number = binary_to_int(bits)
    return number

    
def auxreverseBits(bits,low,high):
    if low < high:
        mid = (low + high)//2
        auxreverseBits(bits,low,mid)
        auxreverseBits(bits,mid+1,high)
        reverse(bits,low,mid,high)


def reverse(bits,low,mid,high):
        n1 = mid - low + 1
        n2 = high - mid
        L = [0] * n1
        R = [0] * n2
        for i in range(n1):
            L[i] = bits[low + i]
        for j in range(n2):
            R[j] = bits[mid + 1 + j]
        i = 0  
        j = 0  
        l = low
        while i < n2:
            bits[l] = R[i]
            i += 1
            l += 1
        while j < n1:
            bits[l] = L[j]
            j += 1
            l +=1

def binary_to_int(binary):
    value = 0
    for bit in binary:
        value = value * 2 + bit
    return value

print(reverseBits(2147483644))
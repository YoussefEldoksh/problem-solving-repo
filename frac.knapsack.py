

def frac_knapsack(A,knapsack_size):
    A.sort(key=lambda x: x[2], reverse=True)
    print(A)
    rev = 0
    for item in A:
        if item[0] <= knapsack_size:
            rev += item[1]
            knapsack_size -= item[0]
        else:
            rev += item[2]*knapsack_size
            return rev
        
    

A = [[1,5,5],[3,10,10/3],[5,15,3],[4,7,7/4],[1,8,8],[3,9,3],[2,4,2]]

print(frac_knapsack(A,15))

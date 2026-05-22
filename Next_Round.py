

def passing_teams(vals,n,k):
    if vals[0] == 0:
        return 0
    for i in range(0,n):
        if vals[i] < vals[k-1] or vals[i] == 0:
            return i
    return n
    
        

n,k = map(int,list(input().split(" ")))

vals = list(map(int, input().split(" ")))


print(passing_teams(vals,n,k))


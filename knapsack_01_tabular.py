
def knapsack(n,items):
    a = len(items)+1
    # create a rows x (n+1) table with independent rows
    c = [[-1 for x in range(n+1)] for _ in range(a)]
    # print(len(c[0]))
    for i in range(a):
        c[i][0] = 0
    for i in range(n+1):
        c[0][i] = 0
    for i in range(1,a):
        for j in range(1,n+1):
            if items[i-1][0] <= j:
                c[i][j] = max(c[i-1][j], items[i-1][1] + c[i-1][j-items[i-1][0]])
            else:
                c[i][j] = c[i-1][j]
    for item in c:
        print(item)
    return c[a-1][n]


A = [[10,60],[20,100],[30,120]]
print(knapsack(50,A))


    # c = [[-1]*(n+1)]*(a)
# Using [[[...]] * a](http://vscodecontentref/2) 
# duplicates a reference to the same inner list a times. 
# All rows point to the same list object, so modifying c[i][j] 
# changes that same list for every row — producing wrong DP updates.


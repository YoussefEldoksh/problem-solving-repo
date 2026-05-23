
def count_moves(matrix):
    x = 0
    y = 0

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                x = abs(i-2)
                y = abs(j-2)
    return x+y


matrix = []
for i in range(5):
    arr = list(map(int,input().split(' ')))
    matrix.append(arr)

print(count_moves(matrix))
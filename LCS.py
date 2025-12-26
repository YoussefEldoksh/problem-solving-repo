def lcs(string_A, string_B):
    sub_string = [[0 for x in range(len(string_A)+1)] for _ in range(len(string_B)+1)]
    for i in range(1, len(string_B)+1):
        for j in range(1, len(string_A)+1):
            if string_A[j-1] == string_B[i-1]:
                sub_string[i][j] = sub_string[i-1][j-1] + 1
            else:
                sub_string[i][j] = max(sub_string[i-1][j], sub_string[i][j-1])
    
    LCS = []
    A = len(string_A)
    B = len(string_B)

    while A > 0 and B > 0:
        if string_A[A-1] == string_B[B-1]:
            LCS.append(string_A[A-1]) 
            A -= 1
            B -= 1
        elif sub_string[B][A-1] > sub_string[B-1][A]:  # Fixed comparison
            A -= 1
        else:
            B -= 1

    LCS.reverse()
    result = ''.join(LCS)
    print(result)
    return result

string_A = "abbcccba"

string_B = "abcccbba"

lcs(string_A, string_B)  # Returns "bcccb"
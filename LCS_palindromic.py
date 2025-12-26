def longestPalindromeSubseq(self, s):
    reversed_s = s[::-1]
    sub_string = [[0 for x in range(len(s)+1)] for _ in range(len(reversed_s)+1)]
    for i in range(1, len(reversed_s)+1):
        for j in range(1, len(s)+1):
            if s[j-1] == reversed_s[i-1]:
                sub_string[i][j] = sub_string[i-1][j-1] + 1
            else:
                sub_string[i][j] = max(sub_string[i-1][j], sub_string[i][j-1])
    return sub_string[i][j]





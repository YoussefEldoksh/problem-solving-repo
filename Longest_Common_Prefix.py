
from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:
    ans = ""

    if len(strs) == 1:
        return strs[0]
    for i in range(len(min(strs, key=len))):
        hashset = set()
        for j in range(len(strs)-1):
            hashset.add(strs[j][i])
        if hashset == {strs[-1][i]}:
            ans += strs[0][i]
        else:
            return ans
    return ans
strs = ["flower","flow","flight"]

print(longestCommonPrefix(None, strs)) 
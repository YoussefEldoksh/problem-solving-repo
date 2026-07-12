
def isPalindrome(s):
    s = s.lower()
    new_s = ""
    for c in s:
        if c.isdigit():
            return False
        if c.isalpha():
            new_s += c
    
    print(new_s)
    
    low = 0
    high = len(new_s)-1
    while low < high:
        if new_s[low] != new_s[high]:
            return False
        low +=1
        high-=1
    
    return True



s = "0P"
print(isPalindrome(s))    



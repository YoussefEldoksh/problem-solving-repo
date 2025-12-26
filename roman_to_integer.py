


def romanToInt(s,low=0):
    if low >= len(s):
        return 0
    values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    if low + 1 < len(s) and values.get(s[low]) < values.get(s[low+1]):
        return -values.get(s[low]) + romanToInt(s,low+1)
    return values.get(s[low])+romanToInt(s,low+1)

print(romanToInt("IV",0))
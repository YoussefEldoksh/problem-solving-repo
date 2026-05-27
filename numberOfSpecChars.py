

def numberOfSpecialChars(word: str): #-> int:
    chars = {}
    vals = {}

    for i in range(len(word)):
        if not word[i].islower() and  chars.get(word[i]) is None:
            chars[word[i]] = i
            print(f"{word[i]}: {i}")
        else:
            vals[word[i]] = 0   

    if len(chars) == 0: return 0 

    for i in range(len(word)):
        if word[i].islower() and chars.get(word[i].upper()):
            indexCompare = chars[word[i].upper()]
            if i < indexCompare:
                vals[word[i]] = 1
            else: vals[word[i]] = 0
        else: continue

    print(chars)
    print(sum(vals.values()))
    return sum(vals.values())


numberOfSpecialChars("ADdadACBC")

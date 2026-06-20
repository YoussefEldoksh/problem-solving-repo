

def groupAnagrams(strs):
    res = {}
    
    for word in strs:
        temp1 = "".join(sorted(word))
        res[temp1] = []

    for j in range(len(strs)):
            
        temp1 = "".join(sorted(strs[j]))    
        if temp1 in res:
                res[temp1].append(strs[j])


        
    print(list(res.values()))
    
    
arr = ["eat","tea","tan","ate","nat","bat"]

groupAnagrams(arr)
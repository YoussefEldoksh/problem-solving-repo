def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashTable1 = {}
        hashTable2 = {}

        for i in range(len(s)):
            hashTable1[s[i]] = 0
        for i in range(len(s)):
            hashTable2[t[i]] = 0

        for i in range(len(s)):
            hashTable1[s[i]] += 1
        for i in range(len(s)):
            hashTable2[t[i]] += 1

        for i in range(len(t)):
            if t[i] not in hashTable1:
                return False
            elif hashTable1[t[i]] != hashTable2[t[i]]:
                return False

        return True

    
isAnagram("anagram", "nagaram")
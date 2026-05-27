class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        for i in range(1,len(word)):
            if (word[i].islower() and not word[i-1].islower() and i-1 != 0) or (not word[i].islower() and  word[i-1].islower()) :
                return False
        return True
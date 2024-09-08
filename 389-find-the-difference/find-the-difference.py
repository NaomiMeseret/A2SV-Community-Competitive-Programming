class Solution:
    from collections import Counter
    def findTheDifference(self, s: str, t: str) -> str:
        countS=Counter(s)
        countT=Counter(t)
        for char in countT:
            if countT[char]!=countS.get(char,0):
                return char
        
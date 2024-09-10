class Solution:
   
    def isAnagram(self, s: str, t: str) -> bool:
        countS=Counter(s)
        countT=Counter(t)
        if len(s)!=len(t):
            return False
        for char in t :
            if countT[char]!=countS[char]:
                return False
        return True
        

        
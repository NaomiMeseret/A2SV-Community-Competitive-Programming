class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLen = float("-inf")
        totalCost = 0
        l = 0
        for r in range(len(s)):
            cost = abs(ord(s[r])-ord(t[r]))
            totalCost+=cost
            while totalCost>maxCost:
                totalCost-=abs(ord(s[l])-ord(t[l]))
                l+=1
            maxLen = max(maxLen,r-l+1)
        if maxLen !=float("-inf"):
            return maxLen
        else:
            return 1
       

        
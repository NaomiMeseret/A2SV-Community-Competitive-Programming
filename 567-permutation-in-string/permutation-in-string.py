class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count=Counter(s1)
        s2Count=Counter(s2[:len(s1)])
        if s1Count==s2Count:
            return True
        for i in range(len(s1),len(s2)):
            s2Count[s2[i]]+=1
            s2Count[s2[i-len(s1)]]-=1
            if s2Count[s2[i-len(s1)]]==0:
                del s2Count[s2[i-len(s1)]]
            if s1Count==s2Count:
                return True
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter=Counter(s1)
        s2Counter=Counter(s2[:len(s1)])
        if s1Counter==s2Counter:
            return True
        for i in range (len(s1),len(s2)):
            s2Counter[s2[i]]+=1
            s2Counter[s2[i-len(s1)]]-=1
            if s2Counter[s2[i-len(s1)]]==0:
                del s2Counter[s2[i-len(s1)]]
            if s2Counter==s1Counter:
                return True
        return False
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_S1 = Counter(s1)
        count_S2 = Counter(s2[:len(s1)])
        if count_S1 == count_S2:
            return True
        l=0
        for r in range(len(s1),len(s2)):
            count_S2[s2[r]] = count_S2.get(s2[r],0)+1
            count_S2[s2[l]]-=1
            if count_S2[s2[l]]==0:
                count_S2.pop(s2[l])
            l+=1
            if count_S2==count_S1:
                return True
        return False
        
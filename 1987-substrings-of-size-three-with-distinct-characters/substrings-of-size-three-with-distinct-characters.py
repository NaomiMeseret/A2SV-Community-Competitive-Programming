class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        count_s=Counter(s[:3])
        if len(s)<3:
            return 0
        if set(count_s.values())=={1}:
            count+=1
        l=0
        for r in range(3,len(s)):
            count_s[s[r]]=count_s.get(s[r],0)+1
            count_s[s[l]]-=1
            if count_s[s[l]]==0:
                count_s.pop(s[l])
            l+=1
            if set(count_s.values())=={1}:
                count+=1
        return count


        
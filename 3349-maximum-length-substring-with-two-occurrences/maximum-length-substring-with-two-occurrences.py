class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        seen={}
        l=0
        max_len=0
        for r in range(len(s)):
            seen[s[r]]=seen.get(s[r],0)+1
            while seen[s[r]]>2:
                seen[s[l]]-=1
                if seen[s[l]]==0:
                    del seen[s[l]]
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
            



        
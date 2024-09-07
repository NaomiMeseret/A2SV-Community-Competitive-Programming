class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for s in strs[1:]:
            length=0
            for i in range(min(len(prefix),len(s))):
                if prefix[i]==s[i]:
                    length+=1
                else:
                    break
            prefix=prefix[:length]
            if not prefix:
                return ""
        return prefix
           

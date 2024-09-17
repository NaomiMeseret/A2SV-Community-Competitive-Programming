class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s):
            return False
        map_pattern = {}
        map_s = {}
        for i in range(len(s)):
            if pattern[i] in map_pattern and map_pattern[pattern[i]] != s[i]:
                return False
            if s[i] in map_s and map_s[s[i]] != pattern[i]:
                return False
            map_pattern[pattern[i]] = s[i]
            map_s[s[i]] = pattern[i]
        
        return True
        
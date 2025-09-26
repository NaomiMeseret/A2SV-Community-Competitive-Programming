class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(i):
            if i == len(s):
                return True 
            if i in memo:
                return memo[i]
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    if dp(i+len(w)):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]
        return dp(0)
        
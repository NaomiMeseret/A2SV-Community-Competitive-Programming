class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        l = 0
        count = 0
        seen = {}
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while max(seen.values(), default=0) >= k:
                count += len(s) - r
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1

        return count



        
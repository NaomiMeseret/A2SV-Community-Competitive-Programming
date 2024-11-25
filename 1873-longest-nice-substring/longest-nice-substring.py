class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        max_len = 0
        result = ""

        for l in range(n):
            seen = set()
            for r in range(l, n):
                seen.add(s[r])
                if all(c.swapcase() in seen for c in seen):
                    if r - l + 1 > max_len:
                        max_len = r - l + 1
                        result = s[l:r + 1]
        return result
        

        
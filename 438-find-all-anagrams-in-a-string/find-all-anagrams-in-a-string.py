class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_P = Counter(p)
        count_S = Counter(s[:len(p)])
        result = []
        if count_P == count_S:
            result.append(0)
        l = 0
        for r in range(len(p), len(s)):
            count_S[s[r]] = count_S.get(s[r], 0) + 1
            count_S[s[l]] -= 1
            if count_S[s[l]] == 0:
                count_S.pop(s[l])
            l += 1
            if count_S == count_P:
                result.append(l)

        return result
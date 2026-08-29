class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result=0
        for char in s:
            if char in t:
                result+=abs(s.index(char)-t.index(char))
        return result

        
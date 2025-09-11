class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        count = 0
        for c in range (m):
            for r in range (n-1):
                if strs[r][c]>strs[r+1][c]:
                    count+=1
                    break
        return count
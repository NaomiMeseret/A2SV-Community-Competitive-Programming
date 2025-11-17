class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        prefix = [[0]*(n +1) for _ in range(m+1)]
        for r in range(m):
            for c in range(n):
                prefix[r+1][c+1] = (prefix[r + 1][c] + prefix[r][c + 1] - prefix[r][c]+ mat[r][c])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)
                total = (prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1]+ prefix[r1][c1])
                ans[i][j] = total
        return ans





           
       
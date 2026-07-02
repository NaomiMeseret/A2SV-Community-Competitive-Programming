class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row,col=len(mat),len(mat[0])
        d=defaultdict(list)
        for i in range(row):
            for j in range(col):
                d[i+j].append(mat[i][j])
        ans= []
        for key, value in d.items():
            if key % 2 == 0:
                ans.extend(value[::-1])
            else:
                ans.extend(value)
        return ans

        
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        top = rows
        bottom = -1
        left = cols
        right = -1
        for i in range(rows):
            for j in range (cols):
                if grid[i][j] == 1:
                    top  = min(top , i)
                    bottom = max(bottom , i)
                    left = min(left , j)
                    right = max(right , j)
        height = bottom-top+1
        width = right-left+1
        area = height*width
        return area
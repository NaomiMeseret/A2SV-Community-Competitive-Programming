class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        perimeter=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    if r == 0 or grid[r - 1][c] == 0: 
                            perimeter += 1
                    if r == row - 1 or grid[r + 1][c] == 0:  
                            perimeter += 1
                    if c == 0 or grid[r][c - 1] == 0:  
                            perimeter += 1
                    if c == col - 1 or grid[r][c + 1] == 0:  
                            perimeter += 1
        return perimeter
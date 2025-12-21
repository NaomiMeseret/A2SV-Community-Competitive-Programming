class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)      
        m = len(strs[0])  
        is_sorted = [False] * (n - 1)
        del_cnt = 0
        for col in range(m):
            is_col_bad = False
            for row in range(n - 1):
                if not is_sorted[row]:
                    if strs[row][col] > strs[row + 1][col]:
                        is_col_bad = True
                        break 
            if is_col_bad:
                del_cnt += 1
            else:
                for i in range(n - 1):
                    if not is_sorted[i] and strs[i][col] < strs[i + 1][col]:
                        is_sorted[i] = True 

        return del_cnt
        
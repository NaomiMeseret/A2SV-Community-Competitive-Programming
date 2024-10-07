class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_opera= float('inf')
        count = 0
        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        min_oper = count
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                count -= 1
            if blocks[i] == 'W':
                count += 1
            min_oper = min(min_oper, count)
        return min_oper
        
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        left = 0
        res = []
        while i >= 0 or j >= 0 or left:
            total = left
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(str(total%2))
            left  = total//2
        return "".join(reversed(res))
        
        
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        l = len(b)
        c = "1"*l
        c = int(c, 2)
        ans = c - n
        return ans
        
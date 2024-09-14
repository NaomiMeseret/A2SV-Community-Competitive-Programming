class Solution:
    import math
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        res=math.log2(n)
        return res.is_integer()
        
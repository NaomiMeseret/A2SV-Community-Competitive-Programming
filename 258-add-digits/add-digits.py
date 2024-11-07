class Solution:
    def addDigits(self, num: int) -> int:
        while num//10 >=1:
            num=sum(int(digit) for digit in str(num))
        return num
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        result=0
        while x>0:
            result*=10
            result+=x%10
            x//=10
        return temp==result

    

        
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        n2 =0
        for num in num1:
            n1=n1*10 
            n1=n1+ord(num)-48
        for num in num2:
            n2=n2*10
            n2= n2+ord(num)-48
        res=n1*n2
        return f"{res}"

        
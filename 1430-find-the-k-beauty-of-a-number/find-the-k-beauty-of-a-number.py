class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count=0
        num=str(num)
        for i in range(len(num)-k+1):
            if int(num[i:i+k])!=0 and int(num)%(int(num[i:i+k]))==0:
                count+=1
        return count

        
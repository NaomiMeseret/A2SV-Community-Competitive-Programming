class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l=0
        countZeros=0
        countOne=0
        count=0
        for r in range(len(s)):
            if s[r]=="0":
                countZeros+=1
            else:
                countOne+=1
            while countZeros>k and countOne>k:
                if s[l]=="0":
                    countZeros-=1
                else:
                    countOne-=1
                l+=1
            count+=r-l+1
        return count
            

                


        
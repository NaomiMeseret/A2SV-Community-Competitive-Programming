class Solution:
    def punishmentNumber(self, n: int) -> int:
        def split(i,curr,target,s):
            if i==len(s):
                return curr == target
            for j in range(i,len(s)):
                if split(j+1,curr+int(s[i:j+1]),target,s):
                    return True
            return False
        ans=0
        for x in range(1,n+1):
            sq=[x*x]
            s=str(sq.pop())
            if split(0,0,x,s):
                ans+=x*x
        return ans
            
        
class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n==0:
            return []
        if n==1:
            return ["0" ,"1"]
        res = ["0" , "1"]
        for _ in range(2,n+1):
            new = []
            for s in res:
                new.append(s +"1")
                if s[-1] == "1":
                    new.append(s+"0")
            res = new
        return res
        

        
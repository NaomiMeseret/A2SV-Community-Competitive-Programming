class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        tCounter=Counter(t)
        sCounter=defaultdict(int)
        l=0
        ans=[0,float("inf")]
        for r in range(n):
            sCounter[s[r]]+=1
            while all(sCounter[char]>= tCounter[char] for char in tCounter):
                if r-l+1<ans[1]-ans[0]+1:
                    ans=[l,r]
                sCounter[s[l]]-=1
                if sCounter[s[l]]==0:
                    del sCounter[s[l]]
                l+=1
        return "" if ans[1] == float("inf") else s[ans[0]:ans[1] + 1]



        
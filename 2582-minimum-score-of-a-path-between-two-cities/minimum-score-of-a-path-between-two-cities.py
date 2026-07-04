class UnionFind():
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if px!=py:
            if self.size[x]<self.size[y]:
                    self.parent[px]=py
                    self.size[py]+=self.size[px]
            else:
                    self.parent[py]=px
                    self.size[px]+=self.size[py]
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        unionfind= UnionFind(n)
        for a,b,c in roads:
            unionfind.union(a,b)
        r=unionfind.find(1)
        ans=float("inf")
        for a,b,c in roads:
            if unionfind.find(a)==r or unionfind.find(b)==r:
                ans=min(ans,c)
        return ans
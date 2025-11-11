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
            if self.size[px]<self.size[py]:
                    self.parent[px]=py
                    self.size[py]+=self.size[px]
            else:
                    self.parent[py]=px
                    self.size[px]+=self.size[py]
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u , v in edges:
            uf.union(u,v)
        nodeCount = defaultdict(int)
        edgeCount = defaultdict(int)
        for node in range(n):
            root = uf.find(node)
            nodeCount[root]+=1
        for u,v in edges:
            root = uf.find(u)
            edgeCount[root]+=1
        res = 0
        for root , k in nodeCount.items():
            n = k*(k-1)//2
            if edgeCount[root] == n:
                res+=1
        return res
        
        
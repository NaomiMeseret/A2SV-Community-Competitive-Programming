class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graphDict = defaultdict(list)
        for u , v in edges:
            graphDict[u].append(v)
            graphDict[v].append(u)
        for node, nei in graphDict.items():
            if len(nei) == len(graphDict)-1:
                return node

        
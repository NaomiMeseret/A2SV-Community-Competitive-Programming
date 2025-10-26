# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parent = {root:None}
        q = deque([root])
        while q:
            n = len(q)
            currLevel = []
            for _ in range(n):
                node = q.popleft()
                currLevel.append(node)
                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    q.append(node.right)
            deepestLevel  = currLevel
        if len(deepestLevel) == 1:
            return deepestLevel[0]
        anc = set(deepestLevel)
        while len(anc)>1:
            anc =set(parent[node] for node in anc)
        return anc.pop()


    
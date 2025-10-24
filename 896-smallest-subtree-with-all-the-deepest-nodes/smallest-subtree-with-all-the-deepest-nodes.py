# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        parent = {root : None}
        q = deque([root])
        while q:
            n = len(q)
            currlevel = []
            for _ in range(n):
                node = q.popleft()
                currlevel.append(node)
                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    q.append(node.right)
            deepest = currlevel
        if len(deepest) == 1:
            return deepest[0]
        anc = set(deepest)
        while len(anc)>1:
            anc = set(parent[node] for node in anc)
        return anc.pop()

        
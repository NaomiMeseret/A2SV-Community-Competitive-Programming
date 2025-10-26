# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        q = deque([root])
        idx = 1
        ansLevel = 1
        maxSum = float("-inf")
        while q:
            levelSum = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                levelSum +=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if levelSum > maxSum:
                maxSum = levelSum
                ansLevel = idx
            idx +=1
        return ansLevel

        
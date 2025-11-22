# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        if not root:
            return None
        q = deque([root])
        current = 1
        while q and current < depth - 1:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            current += 1
        while q:
            node = q.popleft()
            left_old = node.left
            right_old = node.right
            node.left = TreeNode(val)
            node.left.left = left_old
            node.right = TreeNode(val)
            node.right.right = right_old
        return root

            
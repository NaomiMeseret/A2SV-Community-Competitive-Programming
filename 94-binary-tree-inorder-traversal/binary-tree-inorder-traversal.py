# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def preorder(curr):
            if curr:
                preorder(curr.left)
                result.append(curr.val)
                preorder(curr.right)
        preorder(root)
        return result

        
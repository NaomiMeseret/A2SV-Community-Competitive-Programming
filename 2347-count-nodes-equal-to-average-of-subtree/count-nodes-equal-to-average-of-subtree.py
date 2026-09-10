# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def average(node):
            if not node:
                return (0,0)
            leftSum , leftCount = average(node.left)
            rightSum , rightCount = average(node.right)
            totalSum  = leftSum+rightSum+node.val
            totalCount = leftCount+rightCount+1
            if node.val == totalSum//totalCount:
                nonlocal res
                res+=1
            return (totalSum,totalCount)
        res=0
        average(root)
        return res
        
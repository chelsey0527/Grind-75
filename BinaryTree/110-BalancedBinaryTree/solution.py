# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return (self.Height(root) >= 0)
        
    def Height(self, root):

        if root is None: return 0
        left_height, right_height = self.Height(root.left), self.Height(root.right)

        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1: return -1
        return max(left_height, right_height) + 1
        
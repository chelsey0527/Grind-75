# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0

        def depth(node):

            # If there is no node
            if node is None:
                return 0 

            # Find the depth of each side
            left_depth, right_depth = depth(node.left), depth(node.right)

            # Calculate depth
            self.maxDepth = max(left_depth, right_depth) + 1
            
            return self.maxDepth

        depth(root)
        return self.maxDepth
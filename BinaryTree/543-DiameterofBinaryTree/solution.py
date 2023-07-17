# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            
            if node is None:
                return 0 
            
            # Find depth of each side
            left_depth, right_depth = depth(node.left), depth(node.right)

            # Depth = left_depth + right_depth
            self.diameter = max(self.diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter

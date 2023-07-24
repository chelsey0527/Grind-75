# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node): 

            # Node does not exist here
            if node == None: 
                return None

            # Return once we find either p or q
            if node == p or node == q:
                return node
            
            # LCA of p or q on left side
            left = traverse(node.left) 
            # LCA of p or q on right side
            right = traverse(node.right) 
            print('left', left, ' right', right)
            print()

            # LCA of p and q on opposite sides, return the parent
            if left and right: 
                return node

            # Return whichever is the ancestor
            return left or right 

        return traverse(root)
            
            
            
        
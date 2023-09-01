# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # The left and right means boundries
        def valid (node, left, right):
            # Empty tree is BST
            if not node: return True
            # Basic requirement
            if not (node.val < right and node.val > left): return False
            # Check left and right boundries, not subtree
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        # There is no restriction on float numbers
        return valid(root, float('-inf'), float('inf'))
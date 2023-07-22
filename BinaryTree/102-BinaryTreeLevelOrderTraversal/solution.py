# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.ans = []

        def traversal(node, level):

            if node is None:
                return []

            # Check if the current level's list exists, if not, create it
            if len(self.ans) <= level:
                self.ans.append([])
            
            # Append current value into this level
            self.ans[level].append(node.val)

            # Find next level of each side
            traversal(node.left, level+1)
            traversal(node.right, level+1)
            

        traversal(root, 0)
        return self.ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if root is None:
            return []

        # Use a queue for level-order traversal
        queue = [root]


        while queue:
            level_length = len(queue)

            for i in range(level_length):
                print('queue', queue)
                node = queue.pop(0)

                # Append the rightmost node value of each level
                if i == level_length - 1:
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                print('ans-- ', ans)
                print('-----')
        
        return ans

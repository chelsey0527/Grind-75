# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        queue = deque([root])

        while queue:
            level_vals = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level_vals)

        return ans

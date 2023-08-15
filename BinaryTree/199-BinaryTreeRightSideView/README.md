# Binary Tree Right Side View

Problem can be found in [here](https://leetcode.com/problems/binary-tree-right-side-view/)!

### [solution](/BinaryTree/199-BinaryTreeRightSideView/solution.py)

```python
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
                # Pop the left most in the queue
                node = queue.pop(0)

                # Append the rightmost node value of each level
                if i == level_length - 1:
                    ans.append(node.val)
                
                # Add the pop node's left or right child (must in right sequence)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
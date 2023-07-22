# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/maximum-depth-of-binary-tree/)!

### [solution](/BinaryTree/104-MaxDepthOfBinaryTree/solution.py)

```python
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
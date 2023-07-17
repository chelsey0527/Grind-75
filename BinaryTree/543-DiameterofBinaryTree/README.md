# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/diameter-of-binary-tree/)!

### [solution](/BinaryTree/543-DiameterofBinaryTree/solution.py)

```python
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
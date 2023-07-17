# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/balanced-binary-tree/)!

### [solution](/BinaryTree/110-BalancedBinaryTree/solution.py)

```python
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return (self.Height(root) >= 0)
        
    def Height(self, root):

        if root is None: return 0
        left_height, right_height = self.Height(root.left), self.Height(root.right)

        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1: return -1
        return max(left_height, right_height) + 1
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>)
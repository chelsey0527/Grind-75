# Invert Binary Tree

Problem can be found in [here](https://leetcode.com/problems/invert-binary-tree/)!

### [solution](/BinaryTree/226-InvertBinaryTree/README.md)

```python
class Solution(object):
    def invertTree(self, root):

        # Swap from top to down, left to right. From parent to children
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>)
# Validate BST

Problem can be found in [here](https://leetcode.com/problems/validate-binary-search-tree/)!

### [Solution](/BinarySearchTree/98-ValidateBinarySearchTree/solution.py)

```python
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)



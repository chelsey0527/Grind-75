# Lowest Common Ancestor of a Binary Search Tree
Problem can be found in [here](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)!

### [Solution](/BinarySearchTree/235-LowestCommonAncestor/solution.py)

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)



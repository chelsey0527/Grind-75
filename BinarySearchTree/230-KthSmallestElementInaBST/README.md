# Kth Smallest Element in a BST
Problem can be found in [here](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)!

### [Solution](/BinarySearchTree/230-KthSmallestElementInaBST/solution.py)

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0 :
                return cur.val
            cur = cur.right
        
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)



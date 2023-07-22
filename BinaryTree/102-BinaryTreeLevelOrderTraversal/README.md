# Binary Tree Level Order Traversal

Problem can be found in [here](https://leetcode.com/problems/binary-tree-level-order-traversal/)!

### [solution](/BinaryTree/102-BinaryTreeLevelOrderTraversal/solution.py): recursion

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.ans = []

        def traversal(node, level):

            if node is None:
                return []

            # Check if the current level's list exists, if not, create it
            if len(self.ans) <= level:
                self.ans.append([])
            
            # Append current value into this level
            self.ans[level].append(node.val)

            # Find next level of each side
            traversal(node.left, level+1)
            traversal(node.right, level+1)

        traversal(root, 0)
        return self.ans
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
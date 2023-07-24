# Lowest Common Ancestor of a Binary Tree

Problem can be found in [here](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)!

### [solution](/BinaryTree/236-LowestCommonAncestor/solution.py)

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node): 

            # Node does not exist here
            if node == None: 
                return None

            # Return once we find either p or q
            if node == p or node == q:
                return node
            
            # LCA of p or q on left side
            left = traverse(node.left) 
            # LCA of p or q on right side
            right = traverse(node.right) 
            print('left', left, ' right', right)
            print()

            # LCA of p and q on opposite sides, return the parent
            if left and right: 
                return node

            # Return whichever is the ancestor
            return left or right 

        return traverse(root)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
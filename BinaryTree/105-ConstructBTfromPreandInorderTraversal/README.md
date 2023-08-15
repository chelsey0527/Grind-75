# Construct Binary Tree from Preorder and Inorder Traversal

Problem can be found in [here](https://leetcode.com/problems/binary-tree-right-side-view/)!

### [solution](/BinaryTree/105-ConstructBTfromPreandInorderTraversal/solution.py)

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Return directly when only one element
        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
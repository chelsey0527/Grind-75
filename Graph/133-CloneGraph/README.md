# Clone Graph
Problem can be found in [here](https://leetcode.com/problems/clone-graph/description/)!

### [solution](/Graph/133-CloneGraph/solution.py)

```python
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
        
```

Time Complexity: ![O(n+e)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+e)>) (Nodes + edges), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)


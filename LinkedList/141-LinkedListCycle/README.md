# Linked List Cycle

Problem can be found in [here](https://leetcode.com/problems/linked-list-cycle/)!

### [solution](/LinkedList/141-LinkedListCycle/): Two nodes

```python
class Solution(object):
    def hasCycle(self, head):

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: 
                return True
        
        return False

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

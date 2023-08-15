# Reverse Linked List

Problem can be found in [here](https://leetcode.com/problems/reverse-linked-list/)!

### [solution](/LinkedList/206-ReverseLinkedList/)

```python
class Solution(object):
    def reverseList(self, head):
        current = None
        forward = head

        while forward is not None:
            next_node = forward.next
            forward.next = current
            current = forward
            forward = next_node

        return current
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)!

### [solution](/LinkedList/19-RemoveNthNodeFromENdofList/)

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Create a dummy node to handle the case where the head needs to be removed
        dummy = ListNode(0)
        dummy.next = head

        # Use two pointers, fast and slow, to create a gap of n between them
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
# Reorder LinkedList

Problem can be found in [here]([https://leetcode.com/problems/reverse-linked-list/](https://leetcode.com/problems/reorder-list/))!

### [solution](/LinkedList/206-ReverseLinkedList/)

```python
class Solution(object):
    def reorderList(self, head):

        # Check if the list has fewer than three nodes
        if not head or not head.next or not head.next.next:
            return

        # Initialize two pointers, slow and fast, to the head node
        slow, fast = head, head

        # Find the midpoint of the list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Set head2 to the node next to the slow pointer
        head2 = slow.next
        # Break the connection between the first and second halves of the list
        slow.next = None

        # Create a dummy node to construct the reordered list
        dummy = ListNode(0, None)

        # Reverse the second half of the original list
        while head2:
            tmp = head2.next
            head2.next = dummy.next
            dummy.next = head2
            head2 = tmp

        # Set head1 to the head of the original list and head2 to the reversed second half
        head1 = head
        head2 = dummy.next

        # Interleave nodes from the first and second halves of the list
        while head1 and head2:
            tmp = head2
            head2 = head2.next
            tmp.next = head1.next
            head1.next = tmp
            head1 = head1.next.next
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
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

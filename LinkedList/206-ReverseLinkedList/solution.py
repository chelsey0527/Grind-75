class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = None
        forward = head

        while forward is not None:
            next_node = forward.next
            forward.next = current
            current = forward
            forward = next_node

        return current

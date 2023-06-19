class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a new node to serve as the head of the merged list
        # newHead serves as the head of the merged list
        # dummyHead keeps track of the last node
        newHead = dummyHead = ListNode()
        
        # Compare the values of nodes from list1 and list2 and merge them in ascending order
        while list1 and list2:
            if list1.val < list2.val:
                # Connect the smaller node to the merged list
                dummyHead.next = list1
                list1 = list1.next  # Move to the next node in list1
            else:
                # Connect the smaller node to the merged list
                dummyHead.next = list2
                list2 = list2.next  # Move to the next node in list2
            dummyHead = dummyHead.next  # Move the dummyHead to the newly added node
        
        # Connect the remaining nodes of list1 or list2 to the merged list
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2

        # Return the head of the merged list
        return newHead.next

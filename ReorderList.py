# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        ptr1 = head
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        stack1 = []
        stack2 = []

        while ptr1 != slow.next:
            stack1.append(ptr1)
            ptr1 = ptr1.next

        ptr2 = slow.next

        while ptr2:
            stack2.append(ptr2)
            ptr2 = ptr2.next

        stack1 = stack1[::-1]
        ptr1 = head

        while len(stack1) != 0 and len(stack2) != 0:
            ptr1.next = stack1[-1]
            ptr1 = ptr1.next
            stack1.pop()

            ptr1.next = stack2[-1]
            ptr1 = ptr1.next
            stack2.pop()

        while len(stack1) != 0:
            ptr1.next = stack1[-1]
            ptr1 = ptr1.next
            stack1.pop()  

        while len(stack2) != 0:
            ptr1.next = stack2[-1]
            ptr1 = ptr1.next
            stack2.pop()

        ptr1.next = None

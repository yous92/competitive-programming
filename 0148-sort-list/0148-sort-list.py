# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
       
        def findMiddle(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

       
        def merge(l1, l2):
            dummy = ListNode()
            current = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

           
            if l1:
                current.next = l1
            if l2:
                current.next = l2

            return dummy.next

      
        middle = findMiddle(head)
        right_head = middle.next
        middle.next = None 

       
        left = self.sortList(head)
        right = self.sortList(right_head)

       
        return merge(left, right)
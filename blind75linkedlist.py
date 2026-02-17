# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: #empty list
            return head
        
        prev = None
        curr = head

        while curr is not None:
    
            nextNode = curr.next
            
            curr.next = prev

            prev = curr

            curr = nextNode
        
        return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        dummy = ListNode() #dummy node
        prev = dummy

        while curr1 is not None and curr2 is not None:
            

            if curr1.val < curr2.val:
                prev.next = curr1 #set current list tail node 'next' to the current node we are at
                prev = prev.next
                curr1 = curr1.next

            elif curr2.val < curr1.val:
                prev.next = curr2
                prev = prev.next
                curr2 = curr2.next

            else:

                prev.next = curr1
                curr1 = curr1.next

                prev = prev.next
                prev.next = curr2
       


        if curr1 is not None:
            prev.next = curr1
        elif curr2 is not None:
            prev.next = curr2

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seenNodes = set()

        while head:

            if head in seenNodes:
                return True
            else:
                seenNodes.add(head)
                head = head.next
        
        return False

         

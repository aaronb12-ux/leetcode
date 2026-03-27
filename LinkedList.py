# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def getFirstNum():
            """returns reversed number needed for addgin from l1"""
            num1arr = []

            curr = l1
            while curr:
                num1arr.insert(0, curr.val)
                curr = curr.next
            
            return num1arr

        def getSecondNum():
            """returns reversed number needed for addgin from l2"""
            num2arr = []

            curr = l2
            while curr:
                num2arr.insert(0, curr.val)
                curr = curr.next
            
            return num2arr
           
        def createFinalList(num):
            """create a new linked list with number"""
            '''
            iterate through the number and create a new node at each number and connect with pointers
            '''

            head = None
            prev = head
            for n in str(num)[::-1]:
                
                if head == None: #no head yet
                    head = ListNode(int(n))
                    prev = head
                    
                else:
                    newNode = ListNode(int(n))
                    prev.next = newNode
                    prev = newNode
                   
            return head
     

        num1 = int("".join(map(str, getFirstNum())))
        num2 = int("".join(map(str, getSecondNum())))
        total = num1 + num2 

        finalList = createFinalList(total)

        return finalList

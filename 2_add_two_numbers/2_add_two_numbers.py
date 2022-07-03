from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def prepare_link(link):
        head = ListNode(link[0])
        for el in link[1:]:
            node = head
            while node.next:
                node = node.next
            node.next = ListNode(el)
        return head

    def print_linked_list(head) -> None:
        print("[", end="")
        ptr = head
        while ptr:
            print(ptr.val, end=", ")
            ptr = ptr.next
        print("]")


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        temp = None
        carry = 0

        # while two list exists
        while (l1 is not None or 
               l2 is not None):
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val

            _sum = carry + l1_val + l2_val

            # update carry
            carry = 1 if _sum >= 10 else 0

            # update sum
            _sum = _sum if _sum < 10 else _sum % 10

            # create new node with sum
            temp = ListNode(_sum)

            if head is None:
                head = temp
            else:      
                prev.next = temp
          
            prev = temp

            # to the next child nodes of l1 and l2
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if (carry > 0):
            temp.next = ListNode(carry)
        
        return head
            
            
        
if __name__ == "__main__":
    l1 = ListNode.prepare_link([2,4,9])
    ListNode.print_linked_list(l1)

    l2 = ListNode.prepare_link([5,6,4,9])
    ListNode.print_linked_list(l2)

    sol = Solution().addTwoNumbers(l1, l2)
    ListNode.print_linked_list(sol)

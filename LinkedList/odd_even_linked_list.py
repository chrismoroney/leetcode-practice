"""
Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def odd_even_list(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head: 
            return None

        odd = head
        even = head.next
        even_start = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_start
        return head
    
    def convert_head_to_linked_list(self, head):
        list_head = ListNode()
        curr = list_head

        for num in head:
            curr.next = ListNode(num)
            curr = curr.next
        
        return list_head.next
    
    def print_linked_list(self, head):
        curr = head

        while curr:
            print(curr.val, end=" -> " if curr.next else "\n")
            curr = curr.next
    
if __name__ == "__main__":
    head = [2,1,3,5,6,4,7]
    sol = Solution()
    
    linked_list = sol.convert_head_to_linked_list(head)
    sol.print_linked_list(linked_list)
    sol.odd_even_list(linked_list)
    sol.print_linked_list(linked_list)
    

"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverse_list(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        cur = head

        while cur:
            tmp_next = cur.next
            cur.next = prev
            prev = cur
            cur = tmp_next

        return prev

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
    head = [1,2,3,4,5]
    sol = Solution()
    linked_list = sol.convert_head_to_linked_list(head)
    sol.print_linked_list(linked_list)
    reversed_list = sol.reverse_list(linked_list)
    sol.print_linked_list(reversed_list)
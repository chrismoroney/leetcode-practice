"""
Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverse_between(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        current = head
        prev = None

        while left > 1:
            prev = current
            current = current.next
            left -= 1
            right -= 1

        tail = current
        stopper = prev

        while right > 0:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
            right -= 1

        if stopper:
            stopper.next = prev
        else:
            head = prev

        tail.next = current

        return head
    
    def convert_head_to_linked_list(self, head):
        list_head = ListNode()
        curr = list_head

        for num in head:
            curr.next = ListNode(num)
            curr = curr.next
        
        return list_head.next
    
    def print_linked_list(self, linked_list):
        curr = linked_list

        while curr:
            print(curr.val, end=" -> " if curr.next else "\n")
            curr = curr.next

    
if __name__ == "__main__":
    sol = Solution()
    head = [1, 2, 3, 4, 5]
    linked_list = sol.convert_head_to_linked_list(head)

    sol.print_linked_list(linked_list)
    new_list = sol.reverse_between(linked_list, 2, 4)
    sol.print_linked_list(new_list)
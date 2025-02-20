'''
Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def delete_middle(self, head: ListNode) -> ListNode:
        if head.next == None:
            return None

        a, b = head, head.next.next

        while b and b.next:
            a = a.next
            b = b.next.next 
        
        a.next = a.next.next

        return head

    def print_linked_list(self, head: ListNode):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next
    
if __name__ == "__main__":
    head = ListNode(1, next=ListNode(3, next=ListNode(4, next=ListNode(7, next=ListNode(1, next=ListNode(2, next=ListNode(6)))))))
    sol = Solution()

    print("Before: ")
    sol.print_linked_list(head)
    sol.delete_middle(head)
    print("After: ")
    sol.print_linked_list(head)
# Partition List

'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        a_head = a = ListNode(0)
        b_head = b = ListNode(0)

        while head:
            if head.val < x:
                a.next = head
                a = a.next
            else:
                b.next = head
                b = b.next

            head = head.next
        
        b.next = None

        a.next = b_head.next

        return a_head.next

    def print_linked_list(self, head):
            """
            Prints the linked list starting from the given head node.

            :param head: ListNode, the head of the linked list
            """
            current = head
            while current:
                print(current.val, end=" -> " if current.next else "\n")
                current = current.next

if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1, next=ListNode(4, next=ListNode(3, next=ListNode(2, next=ListNode(5, next=ListNode(2))))))
    x = 3

    p = solution.partition(head, x)

    solution.print_linked_list(p)
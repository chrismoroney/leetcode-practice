# Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def merge_two_lists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(-1)

        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 is not None else list2

        return head.next
    
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
    list1 = ListNode(1, next=ListNode(2, next=ListNode(4)))
    list2 = ListNode(1, next=ListNode(3, next=ListNode(4)))  
    solution = Solution()
    merged = solution.merge_two_lists(list1, list2)
    solution.print_linked_list(merged)    
# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    a = l1
    b = l2
    carry_over = 0

    total = ListNode(0)
    current = total

    while a is not None or b is not None:
        sum_val = carry_over

        if a is not None:
            sum_val += a.val
            a = a.next
        if b is not None:
            sum_val += b.val
            b = b.next
        
        carry_over = sum_val // 10

        current.next = ListNode(sum_val % 10)
        current = current.next
    
    if carry_over > 0:
        current.next = ListNode(carry_over)
    
    return total

def print_linkedlist(linked_list):
    current = linked_list
    while current.next is not None:
        print(current.val, "-> ", end="")
        current = current.next
    print(current.val)

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print_linkedlist(l1)
    print_linkedlist(l2)
    print_linkedlist(addTwoNumbers(l1, l2))
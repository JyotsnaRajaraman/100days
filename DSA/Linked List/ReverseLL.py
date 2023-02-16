# Question
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    temp = None
    current = head
    while current != None:
        next = current.next
        current.next = temp
        temp = current
        current = next
    return temp

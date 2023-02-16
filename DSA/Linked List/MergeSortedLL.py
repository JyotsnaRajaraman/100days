# Question
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    if not list1 or not list2:
        return list1 if not list2 else list2
    temp = ListNode()
    list3 = temp
    while list1 and list2:
        if list1.val < list2.val:
            list3.next = list1
            list1 = list1.next
        else:
            list3.next = list2
            list2 = list2.next
        list3 = list3.next

    if list1:
        list3.next = list1
    elif list2:
        list3.next = list2

    return temp.next

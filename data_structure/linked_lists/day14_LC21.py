'''You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.'''

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def combineLinkedList(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.value == list2.value:
            current.next = list1
            current = current.next
            list1 = list1.next
        elif list1.value > list2.value:
            current.next = list2
            current = current.next
            list2 = list2.next
        else:
            current.next = list1
            current = current.next
            list1 = list1.next

    current.next = list1 or list2
    return dummy.next


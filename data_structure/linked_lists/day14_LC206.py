'''Given the head of a singly linked list, reverse the list, and return the reversed list.'''

def reverseLinkedListLOOP(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    
    return previous

def reverseLinkedListRECURSION(head):
    current = head
    if current is None or current.next is None:
        return current
    
    reversed = reverseLinkedListRECURSION(current.next)
    current.next.next = current
    current.next = None

    return reversed
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedlist):
    # Write your code here.
    if linkedlist is None and linkedlist.next is None:
        return
    current = linkedlist
    while current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return linkedlist


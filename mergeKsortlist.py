
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergelist(head1, head2):
    l1 = head1
    l2 = head2
    dummy = Node(-1)
    res = dummy

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            res.next = l1
            res = l1
            l1 = l1.next
        else:
            res.next = l2
            res = l2
            l2 = l2.next

    if l1:
        res.next = l1
    if l2:
        res.next = l2

    return dummy.next

def mergeKLists(listArray):
    head = listArray[0]
    for i in range(1, len(listArray)):
        head = mergelist(head, listArray[i])
    return head

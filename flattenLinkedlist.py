class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.

def mergehe(l1,l2):
    dumy = Node(-1)
    res = dumy
    while(l1 != None and l2 != None):
        if(l1.data <= l2.data):
            res.child = l1
            res = l1
            l1 = l1.child
        else:
            res.child = l2
            res = l2
            l2 = l2.child
        res.child = None
    if(l1):
        res.child = l1
    if(l2):
        res.child = l2
    return dumy.child
def flattenLinkedList(head: Node) -> Node:
    if(head == None or head.next == None):
        return head
    mhead = flattenLinkedList(head.next)
    return mergehe(head,mhead)

'''
    Following is the linked list node structure:
    class Node:
        def __init__(self, data):
        self.data = data
        self.next = None
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def sortTwoLists(first, second):
    l1 = first
    l2 = second
    dumy = Node(-1)
    res = dumy
    while(l1 != None and l2 != None):
        if(l1.data <= l2.data):
            res.next = l1
            res = l1
            l1 = l1.next
        else:
            res.next = l2
            res = l2
            l2 = l2.next
    if(l1):
        res.next = l1
    if(l2):
        res.next = l2
    return dumy.next
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


def convertArray(l):
    head = Node(l[0])
    pre = head
    for i in range(1,len(l)):
        temp = Node(l[i])
        temp.prev = pre
        pre.next = temp
        pre = temp
    return head

def display(r):
    while(r!=None):
        print(r.data)
        r = r.next
        
def deletetail(head):
    if(head == None or head.next == None):
        return None
    else:
        pre = None
        temp = head
        while(temp.next!=None):
            pre = temp
            temp = temp.next
        temp.prev = None
        pre.next = None
        del temp
        return head
l = [2,3,1,5,4]
ll = convertArray(l)
display(ll)
li = deletetail(ll)
display(li)


        
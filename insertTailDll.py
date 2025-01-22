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

def inserttail(head,val):
    if(head == None):
        newNode = Node(val)
        return newNode
    else:
        node = Node(val)
        temp = head
        while(temp.next):
            temp = temp.next
        temp.next = node
        node.prev = temp
    return head


l = [2,3,1,5,4]
ll = convertArray(l)
display(ll)
val = int(input("enter the insert val : "))
li = inserttail(ll,val)
display(li)


        
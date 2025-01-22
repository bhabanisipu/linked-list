class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def convert(l):
    head = Node(l[0])
    movier = head
    for i in range(1,len(l)):
        temp = Node(l[i])
        movier.next=temp
        movier = temp
    return head
def traverse(head):
    temp = head
    while(temp):
        print(temp.data)
        temp = temp.next

def sortf(head):
    if(head == None or head.next == None):
        return head
    newzero = Node(-1)
    newone = Node(-1)
    newtwo = Node(-1)

    zero = newzero
    one = newone
    two = newtwo

    temp = head
    while(temp):
        if(temp.data == 0):
            zero.next = temp
            zero = zero.next
        if(temp.data == 1):
            one.next = temp
            one = one.next
        if(temp.data == 2):
            two.next = temp
            two = two.next
        temp = temp.next
    if(newone.next != None):
        zero.next = newone.next
    else:
        zero.next = newtwo.next
    one.next = newtwo.next
    newNode = newzero.next
    return newNode

l = [0,2,1,2,1,0,2]
head = convert(l)
traverse(head)
print()

l2 = sortf(head)
traverse(l2)


    
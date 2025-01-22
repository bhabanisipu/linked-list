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
def reverse(head):
    if(head == None or head.next == None):
        return head
    newnode = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newnode

def checkpal(head):
    if(head == None or head.next == None):
        return True
    slow = head
    fast = head
    while(fast.next!=None and fast.next.next!=None):
        slow = slow.next
        fast = fast.next.next
    newNode = reverse(slow.next)
    first = head
    second = newNode
    while(second != None):
        if(first.data != second.data):
            reverse(newNode)
            return False
        else:
            first = first.next
            second = second.next
    reverse(newNode)
    return True


l = [2,4,5,4,2]
head = convert(l)
traverse(head)
print()
head1 = checkpal(head)
print(head1)

    
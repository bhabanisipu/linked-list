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

def deletetail(head):
    if(head == None):
        return head
    temp = head
    while(temp.next.next!= None):
        temp=temp.next
    del temp.next
    temp.next=None
    return head
    
l = [2,4,5,3,6]
head = convert(l)
traverse(head)
print(head.data)
ll = deletetail(head)
print()
traverse(ll)

    
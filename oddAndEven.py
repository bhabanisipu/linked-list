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

def oddeven(head):
    if(head == None or head.next == None):
        return head
    odd = head
    even = head.next
    evenval = head.next
    while(even and even.next):
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next
    odd.next = evenval
    return head

l = [2,4,5,3,6,9]
head = convert(l)
traverse(head)
oddeven(head)
print()
traverse(head)

    
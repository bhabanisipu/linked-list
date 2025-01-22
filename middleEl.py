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

def middle(head):
    odd = head
    even = head
    while(even != None and even.next != None):
        odd = odd.next
        even = even.next.next
    return odd
    
l = [2,4,5,3,6,7]
head = convert(l)
traverse(head)
print()
l1 = middle(head)
print(l1.data)

    
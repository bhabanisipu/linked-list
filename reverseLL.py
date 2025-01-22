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
# def reverse(head):
#     if(head == None or head.next == None):
#         return head
#     prev = None
#     temp = head
#     while(temp != None):
#         front = temp.next
#         temp.next = prev
#         prev = temp
#         temp = front
#     return prev

# recursion code
def reverse(head):
    if(head == None or head.next == None):
        return head
    newnode = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newnode
    
l = [2,4,5,3,6]
head = convert(l)
traverse(head)
print()
head1 = reverse(head)
traverse(head1)

    
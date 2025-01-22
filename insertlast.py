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

def insertlast(head,val):
    if(head == None):
        ele = Node(val)
        return ele
    else:
        ele = Node(val)
        temp = head
        while(temp.next):
            temp = temp.next
        temp.next = ele
    return head
    
l = [2,4,5,3,6]
head = convert(l)
traverse(head)
print(head.data)
n = int(input("enter the insert ele : "))
ll = insertlast(head,n)
print()
traverse(ll)

    
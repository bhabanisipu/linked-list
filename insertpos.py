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

def insertpos(head,val,k):
    if(head == None or k==1):
        ele = Node(val)
        ele.next = head
        head = ele
        return head
    
    count = 0
    prev = None
    temp = head
    while(temp):
        ele = Node(val)
        count += 1
        if(count == k):
            prev.next = ele
            ele.next = temp
        else:
            prev = temp
            temp = temp.next
    return head
    
l = [2,4,5,3,6]
head = convert(l)
traverse(head)
print(head.data)
n = int(input("enter the insert ele : "))
k = int(input("enter the element is inserted idex : "))
ll = insertpos(head,n,k)
print()
traverse(ll)

    
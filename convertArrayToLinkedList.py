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
def lenght(head):
    temp = head
    count=0
    while(temp):
        count +=1
        temp = temp.next
    print(count)
def check(head,val):
    temp = head
    flag = False
    while(temp):
        if(temp.data == val):
            flag = True
        temp = temp.next
    if(flag == False):
        print("element not found")
    else:
        print("element is found")
    
l = [2,4,5,3,6]
head = convert(l)
traverse(head)
print(head.data)
lenght(head)
check(head,5)

    
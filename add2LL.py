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
        print(temp.data,end=" ")
        temp = temp.next

def add1(head1,head2):
    t1 = head1
    t2 = head2
    dom = Node(-1)
    temp = dom
    carry = 0
    while(t1 or t2):
        sum = carry
        if(t1): sum += t1.data
        if(t2): sum += t2.data


        node = Node(sum %10)
        carry = sum//10 # because one / this line return float value then we have to // use it return int value

        temp.next = node
        temp = temp.next

        if(t1): t1 = t1.next
        if(t2): t2 = t2.next
    
    if(carry):
        node = Node(carry)
        temp.next = node
    return dom.next
    
l = [2,4,5,3,6]
head1 = convert(l)
traverse(head1)
print()
l1= [3,8,7,6]
head2 = convert(l1)
traverse(head2)
print()
h = add1(head1,head2)
traverse(h)




    
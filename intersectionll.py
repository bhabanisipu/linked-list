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
    return count
# avarage code
# def intersection(t1,t2,d):
#     while(d):
#         d = d-1
#         t2 = t2.next
#     while(t1 != t2):
#         t1 = t1.next
#         t2 = t2.next
#     return t1

# def add(head1,head2):
#     n1 = lenght(head1)
#     n2 = lenght(head2)

#     if(n1<n2):
#         return intersection(head1,head2,n2-n1)
#     else:
#         return intersection(head2,head1,n1-n2)


# optimal code
def add(z1,z2):
    if(z1 == None or z2 == None):
        return None
    t1= z1
    t2 = z2
    while(t1 != t2):
        t1 = t1.next
        t2 = t2.next

        if(t1 == t2):
            return t1
        if(t1 == None): t1 = z2
        if(t2 == None): t2 = z1
    return t1

l = [2,4,5,3,6]
head = convert(l)
traverse(head)
l1 = [1,3,2,4,5]
head2 = convert(l1)
traverse(head2)
print()
t1 = add(head,head2)
print(t1)


    
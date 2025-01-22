class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


def convertArray(l):
    head = Node(l[0])
    pre = head
    for i in range(1,len(l)):
        temp = Node(l[i])
        temp.prev = pre
        pre.next = temp
        pre = temp
    return head

def display(r):
    while(r!=None):
        print(r.data)
        r = r.next

def insert1st(head,val):
    if(head == None):
        newNode = Node(val)
        return newNode
    else:
        node = Node(val)
        temp = head
        node.next = temp
        temp.prev = node
        head = node
    return head
def inserttail(head,val):
    if(head == None):
        newNode = Node(val)
        return newNode
    else:
        node = Node(val)
        temp = head
        while(temp.next):
            temp = temp.next
        temp.next = node
        node.prev = temp
    return head
def insertpos(head,val,k,n):
    if(head == None):
        newNode = Node(val)
        return newNode
    if(k==1):
        return insert1st(head,val)
    if(k==n):
        return inserttail(head,val)
    else:
        temp = head
        count =0
        while(temp):
            count += 1
            if(count == k):
                break
            else:
                temp = temp.next
        ele = Node(val)
        temp1 = temp.prev
        temp1.next = ele
        ele.prev = temp1
        ele.next = temp
        temp.prev = ele
        
    return head
            


l = [2,3,1,5,4]
ll = convertArray(l)
n = len(l)
display(ll)
val = int(input("enter the insert val : "))
k = int(input("enter the insert value in position : "))
li = insertpos(ll,val,k,n)
display(li)


        
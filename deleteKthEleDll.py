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
def delete1st(head):
    if(head == None or head.next == None):
        return None
    else:
        temp = head
        temp1 = temp.next
        temp.next = None
        temp1.prev=None
        head = temp1
        del temp
    return head   
def deletetail(head):
    if(head == None or head.next == None):
        return None
    else:
        pre = None
        temp = head
        while(temp.next!=None):
            pre = temp
            temp = temp.next
        temp.prev = None
        pre.next = None
        del temp
        return head
  
def deletekth(head,k,n):
    if(head == None):
        return None
    if(k == 1):
        return delete1st(head)
    if(k==n):
        return deletetail(head)
    count = 0
    temp = head
    while(temp!=None):
        count = count+1
        if(count == k):
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.prev = None
            temp.next = None
            del temp
            break
        else:
            temp = temp.next
    return head
l = [2,3,1,5,4]
n = len(l)
ll = convertArray(l)
display(ll)
k = int(input("enter the delete position : "))
li = deletekth(ll,k,n)
display(li)


        
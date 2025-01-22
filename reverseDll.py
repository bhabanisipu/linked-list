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
def reverse(head):
    last = None
    temp = head
    while(temp!=None):
        last = temp.prev
        temp.prev = temp.next
        temp.next = last
        temp = temp.prev
    return last.prev     

l = [2,3,1,5,4]
ll = convertArray(l)
display(ll)
li = reverse(ll)
print("reverse the linkedlist : ")
display(li)


        
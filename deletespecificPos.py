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

def deletepos(head,k,n):
    if(k>n):
        return head
    elif(k == 1):
        temp = head
        head = temp.next
        return head
    else:
        count = 0 
        prev = None
        temp = head
        while(temp):
            count += 1
            if(count == k):
                prev.next = temp.next
                del temp
                break
            else:
                prev = temp
                temp = temp.next
        return head
   
    
l = [2,4,5,3,6]
n = len(l)
head = convert(l)
traverse(head)
print(head.data)
ll = deletepos(head,1,n)
print()
traverse(ll)

    
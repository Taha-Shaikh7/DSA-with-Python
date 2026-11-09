class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
head.next.next.next.next=node(50)

def position(value,pos):
    global head
    newnode=node(value)
    if pos==0:
        newnode.next=head
        head=newnode
        

    count=0
    curr=head

    while curr.next is not None:
        count+=1
        curr=curr.next
        if count==(pos-1):
            newnode.next=curr.next
            curr.next=newnode
print("Current linked list: ")
curr=head
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")            

print("Insert at beginning")
position(12,0)

curr=head
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
head.next.next.next.next=node(50)

print("Insert at Middle")
position(14,3)

curr=head
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
head.next.next.next.next=node(50)
print("Insert at End")
position(15,7)
curr=head
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")


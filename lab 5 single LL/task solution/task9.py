class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
head.next.next.next.next=node(50)
def delete(pos):
    global head
    if pos==0:
        head=head.next
        return
    
    curr=head
    count=0
    while curr.next!=None:
        count+=1
        if count==pos:
            curr.next=curr.next.next
            return
        curr=curr.next
    print("This node not exist")


print("Delete first node: ")
delete(0)
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

print("Delete middle node: ")
delete(2)
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

print("Delete last node: ")
delete(4)
curr=head
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")
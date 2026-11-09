class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)

newnode=node(12)

curr=head
while curr.next is not None:
    curr=curr.next
curr.next=newnode


curr=head
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")
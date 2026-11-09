class node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)
node5=node(50)
node6=node(60)
node7=node(70)
node8=node(80)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7
node7.next=node8

head=node1

curr=head
print("None",end=" => ")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")

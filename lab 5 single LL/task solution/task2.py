class node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=node("name1")
node2=node("name2")
node3=node("name3")
node4=node("name4")
node5=node("name5")
node6=node("name6")

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6

curr=node1
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")
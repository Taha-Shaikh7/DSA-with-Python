class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

def up(update_val,pos):
    global head
    curr=head
    count=0
    while curr!=None:
        count+=1
        if count==pos:
            curr.next.data=update_val
        curr=curr.next


up(12,2)
curr=head
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")

print("Explain why linked-list update is not direct indexed access")
print("This is the disadvantage of ll that it is not direct indexed. the nodes are not indexed by 0 to n but the linked by the reference of next node.We cannot directly jump to position 2 or 3.")
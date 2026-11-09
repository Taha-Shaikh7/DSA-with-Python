class node:
    def __init__(self,sap_id):
        self.sap_id=sap_id
        self.next=None
head=node(10001)
head.next=node(10002)
head.next.next=node(10003)
head.next.next.next=node(10004)
head.next.next.next.next=node(10005)
head.next.next.next.next.next=node(10006)
head.next.next.next.next.next.next=node(10007)
head.next.next.next.next.next.next.next=node(10008)

print("Insert one new SAP ID at the beginning and another at the end")
new_node=node(10009)
new_node.next=head
head=new_node

curr=head
while curr!=None:
    if curr==None:
        curr.next=curr.next.next
    curr=curr.next






curr=head
print("None => ",end="")
while curr is not None:
    print(curr.sap_id,end=" => ")
    curr=curr.next
print("None")
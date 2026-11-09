class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
head.next.next.next.next=node(50)

def delete_val(target):
    global head
    if head is None:
        print("list is empty")
        return
    if head.data==target:
        print("This node Exist")
        print(target,"deleted")
        head=head.next
        return
    
    curr=head
    while curr!=None:
        if target==curr.next.data:
            print("This node Exist")
            curr.next=curr.next.next
            print(target,"deleted")
            return
        curr=curr.next
    print("Does not Exist")

delete_val(10)
curr=head
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")

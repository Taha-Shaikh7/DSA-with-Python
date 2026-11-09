class node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Create at least 7 patient token numbers.
patient1=node("patient1")
patient2=node("patient2")
patient3=node("patient3")
patient4=node("patient4")
patient5=node("patient5")
patient6=node("patient6")
patient7=node("patient7")

patient1.next=patient2
patient2.next=patient3
patient3.next=patient4
patient4.next=patient5
patient5.next=patient6
patient6.next=patient7
head=patient1

#Insert an emergency token at the beginning.

def emergency(node_name):
    global head
    newnode=node(node_name)
    newnode.next=head
    head=newnode
emergency("Taha")

#Insert a regular token at the end

def regular(node_name):
    newnode=node(node_name)
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newnode
regular("john")

#Update one token after locating it.

def update(val,pos):
    count=0
    curr=head
    while curr!=None:
        count+=1
        if count==pos:
            curr.data=val
            return
        curr=curr.next
update("kite",3)
    
#Delete one token after locating it.
def delete(node_value):
    global head
    if head.data==node_value:
        head=head.next
        return

    curr=head
    while curr.next!=None:
        if curr.next.data==node_value:
            curr.next=curr.next.next
            return
        curr=curr.next
delete("patient1")

#Display the final linked list.
curr=head
while curr!=None:
    print(curr.data," -> ",end="")
    curr=curr.next

#Provide a short complexity comparison for beginning versus end operations
print("\nInsert an emergency token at the beginning: O(1)")
print("Insert a regular token at the end: O(n)")
print("Update one token after locating it.O(n)")
print("Delete one token after locating it:O(n)")
print("Display the final linked list:O(n)")
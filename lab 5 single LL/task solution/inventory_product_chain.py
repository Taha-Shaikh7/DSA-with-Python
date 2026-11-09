class node:
    def __init__(node,product_id,price):
        node.product_id=product_id
        node.price=price
        node.next=None


node1=node(1222,1000)
node2=node(1223,2000)
node3=node(1224,3000)
node4=node(1225,4000)
node5=node(1226,5000)
node6=node(1227,6000)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
head=node1
curr=head
print("Before")
while curr!=None:
    print(curr.product_id,curr.price," -> ",end="")
    curr=curr.next
#Insert a new product at a specified position
def insert(product_id,price,pos):
    global head
    count=0
    curr=head
    new_node=node(product_id,price)

    if pos==1:
        new_node.next=head
        head=new_node
        return
    if pos>6:
        print("\nInvalid input")
        return
        
    while curr.next!=None:
        count+=1
        
        if count==pos-1:
            new_node.next=curr.next
            curr.next=new_node
            return
        curr=curr.next

insert(123,1001,3)

#Search for a product ID and update its price.
def search(product_id,price):
    curr=head
    while curr!=None:
        if curr.product_id==product_id:
            curr.price=price
            return
        curr=curr.next
search(1223,5432)

#Search for a discontinued product ID and delete that node.
def delete(product_id):
    global head
    if head.product_id==product_id:
        head=head.next
        return
    curr=head
    while curr.next!=None:
        if curr.next.product_id==product_id:
            curr.next=curr.next.next
            return
        curr=curr.next


delete(1226)

print("\nAfter")
curr=head
while curr!=None:
    print(curr.product_id,curr.price," -> ",end="")
    curr=curr.next

print("\nTime and Auxiliary Space Complexity:")
print("Insert: O(n) time, O(1) auxiliary space")
print("Update: O(n) time, O(1) auxiliary space")
print("Delete: O(n) time, O(1) auxiliary space")
print("Display: O(n) time, O(1) auxiliary space")
        

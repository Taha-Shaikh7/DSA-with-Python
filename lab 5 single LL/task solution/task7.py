class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node("name1")
head.next=node("name2")
head.next.next=node("name3")
head.next.next.next=node("name4")
def search(name):
    global head
    curr=head
    while curr is not None:
        if curr.data==name:
            print("Found")
            return
        curr=curr.next
    print("Not found")
        
def update(update_val,pos):
    global head
    curr=head
    count=0
    while curr!=None:
        count+=1
        if count==pos:
            curr.next.data=update_val
        curr=curr.next

search("nam2")
update("ahmed",2)
curr=head
print("None => ",end="")
while curr is not None:
    print(curr.data,end=" => ")
    curr=curr.next
print("None")
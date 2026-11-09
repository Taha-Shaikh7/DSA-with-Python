arr=list(range(100))
## Linear Search
def linear(arr,target):
    comparison=0
    found=False
    for i in range(len(arr)):
        comparison+=1
        if target==arr[i]:
            print("--- Linear Search ---")
            print("Index no:",i)
            print("Total Comparison:",comparison)
            found=True
            break
        
    if found == False:
        print("--- Linear Search ---")
        print("Not found")
        print("Total Comparison:",comparison)
linear(arr,99)

##binary
def binary(arr,target):
    comparison=0
    low=0
    high=len(arr)-1
    found=False
    
    while low<=high:
        mid=(low+high)//2
        comparison+=1
        if arr[mid]==target:
            found=True
            print("--- Binary Search ---")
            print("Index no:",mid)
            print("Total comparison:",comparison)
            return
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    if found ==False:
        print("--- Binary Search ---")
        print("Not found")
        print("Total Comparison:",comparison)


binary(arr,99)

arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def binary(arr,target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            print("Index no:",mid)
            return
        elif arr[mid]<target:
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
    print("Not found")

binary(arr,3)

print("Complexity Analysis: Sorted order is required because binary search decides which half of the array to ignore by comparing the target with the middle value.")
print("Case	Complexity:\nBest case	O(1)\nAverage case	O(log n)\nWorst case    O(log n)")
print("Why O(log n):Because the search space is divided by 2 at every step:")
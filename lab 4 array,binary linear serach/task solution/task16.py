sap_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target=int(input("Enter the target value: "))
def binary(sap_id,target):
    low=0
    high=len(sap_id)-1
    comparisons=0
    while low<=high:
        mid=(low+high)//2
        comparisons+=1

        if sap_id[mid]==target:
            
            print(sap_id[mid],"Found")
            print("Total comparisons:",comparisons)
            return
        
        elif sap_id[mid]<target:
            
            low=mid+1

        elif sap_id[mid]>target:
            
            high=mid-1

    print("Not found")

binary(sap_id,target)
print("Complexity Analysis: Sorted order lets you cut your search list in half every single time you check the middle number because you know for sure which side your target number is on.")
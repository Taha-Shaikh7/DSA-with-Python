import time
sap_id=[100,323,221,543,666,213,236,788,865,656,986,345,341,521,415,525,532,665,633,653,651]

#linear search
def linear_search(target):
    comparsion=0
    make=False

    start=time.perf_counter()
    for i in sap_id:
        
        comparsion+=1
        if i==target:
            make=True
            print("Index no:",sap_id.index(i))
            break
        end=time.perf_counter()

    print("Total Comparsion:",comparsion)
    print("Execution time:",end-start)
    
    if make==False:
        print("Element not found")
        print("Total Comparsion:",comparsion)

linear_search(666)

#binary search

def binary_search(target):
    sap_id.sort()

    low=0
    high=len(sap_id)-1
    comparison=0
    found=False
    start=time.perf_counter()
    while low<=high:
        mid=(low+high)//2
        comparison+=1

        if sap_id[mid]==target:
            found=True
            print("Index no:",mid)
            print("Total comparison:",comparison)
            break
       
        elif target<sap_id[mid]:
            high=mid-1
       
        else:
            low=mid+1
        end=time.perf_counter()
    
    print("Execution time:",end-start)
    if found==False:
        print("Element not found")
        print("Total comparison:",comparison)
binary_search(666)

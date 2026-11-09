product_id=[1014,1023,1032,1004,1015,1012,1077,1018,1076,1013,1028,1009,1044,1055,1067]

def linear_search(product_id,target):
    exist=False
    camparison=0
    for i in range(len(product_id)):
        camparison+=1
    
        if target==product_id[i]:
            print("This ID exists")
            print("Position at:",i)
            print("Total comparions are:",camparison)
            exist=True
            break
    if not exist:
        print("This ID not exist")
print("Test a target near the beginning: ")
linear_search(product_id,1002)
print("Complexity Analysis: O(1) Best Case")

print("Test a target near the end: ")
linear_search(product_id,1014)
print("Complexity Analysis: O(n) Worst Case")

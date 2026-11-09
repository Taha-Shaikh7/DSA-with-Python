num=[1,2,3,4,5,6,7,8,9,10,11,12]
target=int(input("Enter the number to search: "))
found=False
for i in num:
    if i==target:
        print(f"Index number of element {target} is:",num.index(target))
        found=True
        break

if not found:
    print("Not-found")
print("Complexity Analysis:\nBest Case:O(1) Targeted element is at first position ")
print("Average Case: O(n) Targeted element is at middle position")
print("Worst Case: O(n) targeted element is at last position")
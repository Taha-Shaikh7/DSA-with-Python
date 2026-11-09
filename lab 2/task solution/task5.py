import time
num=[1,2,3,5,2,3]
start=time.perf_counter()
duplicate=False

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]==num[j]:
            print("Duplicate numbers are:",num[i])
            duplicate=True
    end=time.perf_counter()
if not duplicate:
    print("No Duplicate Value")
print("Execution time:",end-start)
print("Time Complexity: O(n)^2")

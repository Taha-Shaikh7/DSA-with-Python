import time
num=[10,20,30,40,50]
start=time.perf_counter()
for i in range(len(num)):
    num[i]=num[i]+5
end=time.perf_counter()
print("After update: ",num)
print("Time Complexity is O(1)")
print("Execution time is: ",end-start)
print("Auxiliary space complexity is: O(1)")

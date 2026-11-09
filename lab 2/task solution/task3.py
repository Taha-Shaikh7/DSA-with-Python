import time
size=[2,3,4,5]
for n in size:
    start=time.perf_counter()
    print(f"\nMultiplication table from 1 to {n}\n")
    for i in range(1,n+1): #loop runs n times
        print(f"Table of",i)
        for j in range(1,11): #this loop runs 10 times
            print(i*j,end=" ")
        print()
    end=time.perf_counter()
print("Time of Execution: ",end-start)
print("Time Complexity: O(n)")

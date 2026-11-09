import time
def sum(num):
    total=0
    for i in num:
        total+=i
    return total
size=[10,22,3,5,66]
for i in size:
    num=list(range(1,i+1))
    start=time.perf_counter()
    result=sum(num)
    end=time.perf_counter()
    print(f"Sum of {i} numbers is: ",end="")
    print(result)
    print("Time of Execution: ",end-start)
    print("Time Complexity: O(n)")

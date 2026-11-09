import time
import random
def student(marks):
    count=0
    for i in marks:
        if i>=50:
            count+=1
    return count

for n in [100,500,1000,2000]:
    marks=[random.randint(0,100) for i in range(n)]
    
    start=time.perf_counter()
    passed=student(marks)
    end=time.perf_counter()
    
    print("N=",n)
    print("Students marks>=50 is:",passed)
    print("Auxiliary Space Complexity: O(1)")
    print("Execution time is:",end-start)
    print()

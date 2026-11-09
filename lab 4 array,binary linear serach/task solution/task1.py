import time
marks=[10,20,30,40,50,60,70,80,90,100]
start=time.perf_counter()
marks.append(101)
end=time.perf_counter()
print(marks)
print("Time Complexity is O(1)")
print("because no any element shifting occurs.It is direct access")
print("Execution time is: ",end-start)
print("Auxiliary space complexity is: O(1)")
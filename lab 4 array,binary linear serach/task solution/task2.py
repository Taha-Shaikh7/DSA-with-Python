import time
marks=[10,20,30,40,50,60,70,80,90,100]
start=time.perf_counter()
marks.insert(0,101)
end=time.perf_counter()
print(marks)
print("Time Complexity is O(n)")
print("Element shifting occurs.Reset of all 10 elements shift one position to the right.It is not direct access")
print("Execution time is: ",end-start)
print("Auxiliary space complexity is: O(1)")
import time
marks=[10,20,30,40,50,60,70,80,90,100]
mid=len(marks)//2
start=time.perf_counter()
marks.insert(mid,101)
end=time.perf_counter()
print(marks)
print("Time Complexity is O(n)")
print("Element shifting occurs.\nInsertion position:New mark is added in middle index. Reset of 5 elements shift one position to the right.It is not direct access")
print("Execution time is: ",end-start)
print("Auxiliary space complexity is: O(1)")

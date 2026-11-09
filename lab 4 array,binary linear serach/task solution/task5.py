import time
student=["name1","name2","name3","name4","name5"]
start=time.perf_counter()
student.pop()
end=time.perf_counter()
print(student)
print("Time Complexity is O(1)")
print("Complexity Analysis: No Element shifting occurs.\nBecause there is nothing after last element.It is direct access")
print("Execution time is: ",end-start)
print("Auxiliary space complexity is: O(1)")

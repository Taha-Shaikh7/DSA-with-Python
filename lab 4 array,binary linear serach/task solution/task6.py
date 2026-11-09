import time
name=["name1","name2","name3","name4","name5"]
start=time.perf_counter()
name.pop(0)
end=time.perf_counter()
print("After deleting: ",name)
print("Time Complexity is O(1)")
print("Complexity Analysis: After deleting index 0, every element shift left by 1 position.the number of shifts grows linearly with the size of array")
print("Execution time is: ",end-start)
print("Auxiliary space complexity is: O(1)")

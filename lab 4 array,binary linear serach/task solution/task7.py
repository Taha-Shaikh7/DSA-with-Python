import time
name=["name1","name2","name3","name4","name5","name6","name7","name8","name9","name10"]
mid=int(len(name)/2)
start=time.perf_counter()
name.pop(mid)
end=time.perf_counter()
print("After deleting: ",name)
print("Time Complexity is O(n)")
print("Complexity Analysis: After deleting middle index, last 4 element shift left by 1 position.The number of shifts grows linearly with the size of array")
print("Count the shift: ",len(name)-mid)
print("Execution time is: ",end-start)
print("Auxiliary space complexity is: O(1)")

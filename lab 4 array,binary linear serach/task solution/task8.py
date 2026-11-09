import time
name=["name1","name2","name3","name4","name5","name6","name7","name8","name9","name10"]
mid=int(len(name)/2)

start=time.perf_counter()
name.pop(8)
end=time.perf_counter()

print("After deleting specified index: ",name)
print("Time Complexity is O(1)")
print("Complexity Analysis: After deleting specified index, last element shift left by 1 position.The number of shifts grows linearly with the size of array")
print("Auxiliary space complexity is: O(1)")
print("Execution time is: ",end-start)

print()
name=["name1","name2","name3","name4","name5","name6","name7","name8","name9","name10"]

start1=time.perf_counter()
name.pop(0)
end1=time.perf_counter()

print("After deleting beginning index: ",name)
print("Time Complexity is O(n)")
print("Complexity Analysis: After deleting index 0, every element shift left by 1 position.the number of shifts grows linearly with the size of array")
print("Auxiliary space complexity is: O(1)")
print("Execution time is: ",end1-start1)
print()
name=["name1","name2","name3","name4","name5","name6","name7","name8","name9","name10"]

start2=time.perf_counter()
name.pop()
end2=time.perf_counter()
print("After deleting last index: ",name)
print("Time Complexity is O(1)")
print("Complexity Analysis: After deleting last index, every element shift left by 1 position.the number of shifts grows linearly with the size of array")
print("Execution time is: ",end2-start2)
print("Auxiliary space complexity is: O(1)")
print()
name=["name1","name2","name3","name4","name5","name6","name7","name8","name9","name10"]

start3=time.perf_counter()
name.pop(mid)
end3=time.perf_counter()

print("After deleting: ",name)
print("Time Complexity is O(n)")
print("Complexity Analysis: After deleting middle index, last 4 element shift left by 1 position.The number of shifts grows linearly with the size of array")
print("Auxiliary space complexity is: O(1)")
print("Execution time is: ",end3-start3)

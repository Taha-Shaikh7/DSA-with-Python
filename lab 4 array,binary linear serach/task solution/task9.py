import time
name=["name1","name2","name3","name4","name5","name6","name7","name8","name9","name10"]
start=time.perf_counter()
name[3]="john"
name[5]="dude"
name[9]="pink"
end=time.perf_counter()
print("After update: ",name)
print("Time Complexity is O(1)")
print("Execution time is: ",end-start)
print("Auxiliary space complexity is: O(1)")

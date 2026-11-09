import time
student_name=["name1","name2","name3","name4","name5"]

print("Delete an element from the end")
print("Current list: ",student_name)
start=time.perf_counter()
student_name.pop()
end=time.perf_counter()
ending=end-start
print("After Deleting:",student_name)
print("Execution time:",ending)
print("Time Complexity is: O(1) Because No any element is shifted")
print("Auxillary time complexity: O(1)")

student_name=["name1","name2","name3","name4","name5"]
print("\nDelete an element from the beginning")
print("Current list: ",student_name)
start1=time.perf_counter()
student_name.pop(0)
end1=time.perf_counter()
beg=end1-start1
print("After Deleting:",student_name)
print("Execution time:",beg)
print("Time Complexity is: O(n) Because we deleted 1st element from the list then remaining elements shifted leftAs the list size increases the number of shifted elements also increases.")
print("Auxillary time complexity: O(1)")


student_name=["name1","name2","name3","name4","name5"]
print("\nDelete an element from the specified middle index")
print("Current list: ",student_name)
start2=time.perf_counter()
student_name.pop(len(student_name)//2)
end2=time.perf_counter()
mid=end2-start2
print("After Deleting:",student_name)
print("Execution time:",mid)
print("Time Complexity is: O(n) Because we deleted middle element from the list then remaining elements shifted left As the list size increases the number of shifted elements also increases.")
print("Auxillary time complexity: O(1)")
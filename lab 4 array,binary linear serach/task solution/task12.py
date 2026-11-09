students=["name1","name2","name3","name4","name5"]
print("Current students:",students)
students.insert(3,"john")
students.remove("name3")
students[0]="jony"
print("Final list is: ",students)
print("Complexity of locating a student when only the name is known: O(n)")
print("Complexity Analysis for insertion: O(n)")
print("Complexity Analysis for deletion: O(n)")
print("Complexity Analysis for updation: O(1)")
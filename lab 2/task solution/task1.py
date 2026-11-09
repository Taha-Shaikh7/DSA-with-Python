import time

student={
    "Name":"john",
    "Department":"AI",
    "Age":18,
    "Semester":3
}
start=time.perf_counter()
semester=student.get("Semester")
end=time.perf_counter()
print("Student Semester:",semester)
print("Time of Execution:",end-start,"Second")
print("Time Complexity: O(1)")
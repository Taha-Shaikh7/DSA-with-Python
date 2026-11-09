import time
marks=[10,20,30,40,50,60,70,80,90,100]
mid=len(marks)//2
user=int(input("Enter the index number(0-9): "))
mark=int(input("Enter the marks: "))

start=time.perf_counter()
marks.insert(user,mark)
end=time.perf_counter()

if user==0:
    print("User input at beginning")
    print(marks)
    print("Time Complexity is O(1)")
    print("No Element shifting occurs.It is direct access")
    print("Execution time is: ",end-start)
    print("Auxiliary space complexity is: O(1)")
    

elif user==mid:
    print("User input at middle")
    print(marks)
    print("Time Complexity is O(n)")
    print("Element shifting occurs.\nNew mark is added in middle index.Rest of 5 elements shift one position to the right.It is not direct access")
    print("Execution time is: ",end-start)
    print("Auxiliary space complexity is: O(1)")

elif user==9:
    print(marks)
    print("User input at the end")
    print("Time Complexity is O(1)")
    print("because no any element shifting occurs.It is direct access")
    print("Execution time is: ",end-start)
    print("Auxiliary space complexity is: O(1)")

else:
    print("Invalid")
import time
temp=[45,34,25,23,12,51,35]
print("Dialy temperature:",temp)
max=temp[0]
for i in temp:
    if max<i:
        max=i
print("Highest temperature is:",max)
min=temp[0]
for i in temp:
    if min>i:
        min=i
print("Lowest temperature is:",min)
print("Total Temperature is:",sum(temp))
print("Average temperature is:",float(sum(temp)/len(temp)))
print("Time Complexity: O(n)")
print("Complexity Analysis: O(n)+O(n)+O(n)= O(3n)= O(n) constant idnored in big O notation")
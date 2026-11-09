import time
mark=[1,2,3,4,5,6]
def high(mark):
    maxi=max(mark)
    return maxi
start=time.perf_counter()
highest=high(mark)   
end=time.perf_counter()
print("Highest value in list:",highest)     
print("Time Complexity is O(1)")
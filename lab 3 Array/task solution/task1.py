import time
Sap=[1120,1121,1122,1123,1124,1125,1126,1127,1128,1129]
start=time.perf_counter()
print(Sap[0],Sap[5],Sap[-1])
end=time.perf_counter()
print("Execution Time: ",end-start)
print("Time Complexity: O(1)")
print("Auxillary Space Complexity: O(1)")
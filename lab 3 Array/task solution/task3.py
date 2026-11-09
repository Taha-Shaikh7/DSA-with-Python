import time
size=[5,8,9,10]
for n in size:
    marks=[20]*n
    start=time.perf_counter()
    marks.append(22)
    end=time.perf_counter()

    ending=end-start
    print("N =",n)
    print()
    print("Insert at end:",marks)
    print("Execution time:",ending)
    

    marks=[20]*n
    start1=time.perf_counter()
    marks.insert(0,33)
    end1=time.perf_counter()

    beg=end1-start1

    print("Insert at beginning:",marks)
    print("Execution time:",beg)
    


    marks=[20]*n
    start2=time.perf_counter()
    marks.insert(len(marks)//2,44)
    end2=time.perf_counter()

    mid=end2-start2


    print("Insert at middle index:",marks)
    print("Execution time:",mid)    
    print()
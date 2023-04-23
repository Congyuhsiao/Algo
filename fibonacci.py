import random

def fibMonaccianSearch(arr, x, n):
    fibMMm2 = 0 
    fibMMm1 = 1 
    fibM = fibMMm2 + fibMMm1 

    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1

    while (fibM > 1):
        i = min(offset+fibMMm2, n-1)
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
    if(fibMMm1 and arr[n-1] == x):
        return n-1
    return -1

for i in range(10,1000,10):
    arr = random.sample(range(1000),i)
    x = random.randint(1, 1000)
    n = len(arr)
    result = fibMonaccianSearch(arr, x, n)
    print(arr)
    print(x)
    if(result >= 0):
        print("Found at index:",result)
    else:
        print(x,"isn't present in the array")

import random

def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

for i in range(10,1000,10):
    array = random.sample(range(1000),i)
    x = random.randint(1, 1000)
    n = len(array)
    result = linearSearch(array, n, x)
    print(array)
    if(result == -1):
        print("Element not found")
    else:
        print("Element found at index: ", result)
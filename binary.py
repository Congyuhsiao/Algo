import random
def binarySearch(arr, l, r, x):
	while l <= r:
		mid = l + (r - l) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return -1

for i in range(10,1000,10):
    arr = random.sample(range(1000),i)
    x = random.randint(1,1000)
    result = binarySearch(arr, 0, len(arr)-1, x)
    print(arr)
    print(x)
    if(result != -1):
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

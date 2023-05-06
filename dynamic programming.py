import time
import matplotlib.pyplot as plt

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dynamic(n):
    fib_array = [0, 1]
    for i in range(2, n+1):
        fib_array.append(fib_array[i-1] + fib_array[i-2])
    return fib_array[n]

n_values = range(10, 101, 10)
recursive_times = []
dynamic_times = []

for n in n_values:
    start_time = time.time()
    fib_recursive(n)
    end_time = time.time()
    recursive_times.append(end_time - start_time)
    start_time = time.time()
    fib_dynamic(n)
    end_time = time.time()
    dynamic_times.append(end_time - start_time)

plt.plot(n_values, recursive_times, label='Recursive')
plt.plot(n_values, dynamic_times, label='Dynamic')
plt.legend()
plt.xlabel('n')
plt.ylabel('Execution Time (s)')
plt.show()

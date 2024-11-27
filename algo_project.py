import numpy as np
import time
import matplotlib.pyplot as plt

def generate_random_array(n):
    return np.random.randint(0, 10000, size=n)

def HybridSort(A, K):
    if len(A) <= K:
        InsertionSort(A)
    else:
        Merge_Sort(A, K)

def Merge_Sort(arr, K):
    if len(arr) <= K:
        InsertionSort(arr)
    elif len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        Merge_Sort(left, K)
        Merge_Sort(right, K)

        merge(arr, left, right)

def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def run_experiment(n_values, k_values, num_runs=5):
    avg_times = {}
    for n in n_values:
        avg_times[n] = []
        for K in k_values:
            times = []
            for _ in range(num_runs):
                arr = generate_random_array(n)
                start_time = time.time()
                HybridSort(arr, K)
                times.append(time.time() - start_time)
            avg_times[n].append(np.mean(times))
    return avg_times

n_values = [1000, 5000, 10000, 15000, 25000]
k_values = list(range(1, 101))

avg_times = run_experiment(n_values, k_values)

plt.figure(figsize=(10, 6))
for n in n_values:
    plt.plot(k_values, avg_times[n], label=f'n = {n}')
plt.xlabel('K (Threshold for Insertion Sort)')
plt.ylabel('Average Time (Seconds)')
plt.title('Hybrid Sort Average Time as a Function of K and n')
plt.legend()
plt.show()
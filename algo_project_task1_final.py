import numpy as np
import time
import matplotlib.pyplot as plt

#Task 1
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


#Task 2
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

#Task 3
# Identify optimal K for each value of n
optimal_ks = []
for n in n_values:
    runtimes_for_n = avg_times[n]  # Average runtimes for this n
    optimal_k = k_values[np.argmin(runtimes_for_n)]  # Find K with minimum runtime
    optimal_ks.append(optimal_k)

# Plot optimal K as a function of n
plt.figure(figsize=(10, 6))
plt.plot(n_values, optimal_ks, marker='o')
plt.xlabel('Array Size (n)')
plt.ylabel('Optimal Threshold (K)')
plt.title('Optimal K as a Function of Array Size (n)')
plt.grid()
plt.show()

#Task 4
def run_experiment_sorted(n_values, k_values, num_runs=5):
    avg_times_sorted = {}
    for n in n_values:
        avg_times_sorted[n] = []
        for K in k_values:
            times = []
            for _ in range(num_runs):
                arr = np.arange(n)  # Pre-sorted array
                start_time = time.time()
                HybridSort(arr, K)
                times.append(time.time() - start_time)
            avg_times_sorted[n].append(np.mean(times))
    return avg_times_sorted


avg_times_sorted = run_experiment_sorted(n_values, k_values)

# Compare the results with random arrays
plt.figure(figsize=(10, 6))

for n in n_values:
    plt.plot(k_values, avg_times_sorted[n], label=f'n = {n}')
plt.xlabel('K (Threshold for Insertion Sort)')
plt.ylabel('Average Time (Seconds)')
plt.title('Hybrid Sort: Sorted Arrays')
plt.legend()

plt.tight_layout()
plt.show()

#Optimal K for Sorted Array Plot:
optimal_ks = []
for n in n_values:
    runtimes_for_n = avg_times_sorted[n]  # Average runtimes for this n
    optimal_k = k_values[np.argmin(runtimes_for_n)]  # Find K with minimum runtime
    optimal_ks.append(optimal_k)

# Plot optimal K as a function of n
plt.figure(figsize=(10, 6))
plt.plot(n_values, optimal_ks, marker='o')
plt.xlabel('Array Size (n)')
plt.ylabel('Optimal Threshold (K)')
plt.title('Optimal K as a Function of Array Size (n)')
plt.grid()
plt.show()

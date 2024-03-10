import time
import random
import matplotlib.pyplot as plt

def BubbleSort(arr):
    numbersSize = len(arr)
    for i in range(numbersSize - 1):
        for j in range(numbersSize - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        start = start + 1

def measure_time(func, arr):
    start_time = time.time()
    func(arr.copy())
    end_time = time.time()
    return end_time - start_time

def generate_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

def benchmark_sorts(sorts, sizes, iterations=10):
    print("Starting benchmark...")
    results = {sort.__name__: [] for sort in sorts}
    stats = {sort.__name__: {'total_time': 0, 'average_time': 0, 'iterations': iterations} for sort in sorts}

    for index, size in enumerate(sizes):
        print(f"Processing size: {size} ({index + 1}/{len(sizes)})")
        temp_results = {sort.__name__: [] for sort in sorts}
        for iteration in range(iterations):
            print(f"\tIteration: {iteration + 1}/{iterations}")
            arr = generate_array(size)
            for sort in sorts:
                exec_time = measure_time(sort, arr)
                temp_results[sort.__name__].append(exec_time)

        for sort_name, times in temp_results.items():
            avg_time = sum(times) / len(times)
            results[sort_name].append(avg_time)
            stats[sort_name]['total_time'] += avg_time

    print("Benchmark complete.")
    return results, stats

def plot_results(results, sizes):
    plt.figure(figsize=(10, 6))
    for sort_name, times in results.items():
        plt.plot(sizes, times, label=sort_name)

    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithm Performance Across Different Sizes')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

def print_statistics(stats):
    for sort_name, data in stats.items():
        print(f"\n{sort_name} Statistics:")
        print(f"Total Execution Time across all sizes: {data['total_time']:.6f} seconds")
        print(f"Average Execution Time per size: {data['average_time']:.6f} seconds")
        print(f"Number of iterations: {data['iterations']}")

def main():
    sorts = [BubbleSort, cocktailSort]
    sizes = [10, 100, 1000, 5000, 10000, 12500]
    iterations = 30  

    results, stats = benchmark_sorts(sorts, sizes, iterations)
    plot_results(results, sizes)
    print_statistics(stats)

if __name__ == "__main__":
    main()


import random
import time

# ---------------- INSERTION SORT ----------------
def insertion_sort(arr):
    # Traverse from second element
    for i in range(1, len(arr)):
        key = arr[i]   # Current element
        j = i - 1

        # Move elements greater than key one step ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at correct position
        arr[j + 1] = key

    return arr


# ---------------- MERGE SORT ----------------
def merge_sort(arr):
    if len(arr) > 1:

        # Find middle index
        mid = len(arr) // 2

        # Divide array into two halves
        left = arr[:mid]
        right = arr[mid:]

        # Recursive calls
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


# ---------------- QUICK SORT ----------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Take first element as pivot
    pivot = arr[0]

    # Elements smaller than pivot
    left = [x for x in arr[1:] if x <= pivot]

    # Elements greater than pivot
    right = [x for x in arr[1:] if x > pivot]

    # Recursive sorting
    return quick_sort(left) + [pivot] + quick_sort(right)


# ---------------- DATASET GENERATION ----------------
def generate_data(size):

    # Random dataset
    random_data = [random.randint(1, 10000) for _ in range(size)]

    # Already sorted dataset
    sorted_data = list(range(size))

    # Reverse sorted dataset
    reverse_data = list(range(size, 0, -1))

    return random_data, sorted_data, reverse_data


# ---------------- TIME MEASUREMENT ----------------
def calculate_time(sort_function, data):

    # Copy dataset to avoid modifying original
    arr = data.copy()

    start = time.time()

    # Call sorting function
    if sort_function == quick_sort:
        sort_function(arr)
    else:
        sort_function(arr)

    end = time.time()

    return end - start


# ---------------- MAIN PROGRAM ----------------
sizes = [1000, 5000, 10000]

for size in sizes:

    print("\n==============================")
    print("Dataset Size:", size)
    print("==============================")

    random_data, sorted_data, reverse_data = generate_data(size)

    datasets = {
        "Random": random_data,
        "Sorted": sorted_data,
        "Reverse": reverse_data
    }

    for name, data in datasets.items():

        print(f"\n{name} Data:")

        # Insertion Sort Time
        t1 = calculate_time(insertion_sort, data)
        print("Insertion Sort Time:", round(t1, 5), "seconds")

        # Merge Sort Time
        t2 = calculate_time(merge_sort, data)
        print("Merge Sort Time:", round(t2, 5), "seconds")

        # Quick Sort Time
        t3 = calculate_time(quick_sort, data)
        print("Quick Sort Time:", round(t3, 5), "seconds")
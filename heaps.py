# Given an array, find the minimum element using a Min-Heap.
import heapq

def find_minimum(arr):
    if not arr:
        raise ValueError("Array is empty")
    # Convert the array into a Min-Heap
    heapq.heapify(arr)
    # The smallest element is at the root of the heap
    return arr[0]

# Example usage:
arr = [5, 3, 8, 1, 2]
print(find_minimum(arr))  # Output: 1



# Given an array and an integer k, find the k smallest elements


def k_smallest_elements(arr, k):
    if k >= len(arr):
        # If k is greater than or equal to the length of the array, return a sorted array
        return sorted(arr)
    # Use a Max-Heap (inverted values) to track the k smallest elements
    max_heap = [-x for x in arr[:k]]  # Convert values to negative for Max-Heap
    heapq.heapify(max_heap)
    for num in arr[k:]:
        if -num > max_heap[0]:
            heapq.heappushpop(max_heap, -num)
    # Convert values back to positive and sort
    return sorted(-x for x in max_heap)

# Example usage:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(k_smallest_elements(arr, k))  # Output: [3, 4, 7]




# Merge two sorted arrays into a single sorted array using a Min-Heap.



def merge_sorted_arrays(arr1, arr2):
    # Use heapq.merge to merge two sorted arrays
    return list(heapq.merge(arr1, arr2))

# Example usage:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]


# Find the k largest elements in an array.
import heapq

def top_k_elements(arr, k):
    if k <= 0:
        return []
    if k >= len(arr):
        # If k is greater than or equal to the length of the array, return a sorted array in descending order
        return sorted(arr, reverse=True)
    # Use heapq.nlargest to find the k largest elements
    return heapq.nlargest(k, arr)

# Example usage:
arr = [5, 1, 7, 9, 2, 6]
k = 3
print(top_k_elements(arr, k))  # Output: [9, 7, 6]



# The main function to sort an array of given size








def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left child
    r = 2 * i + 2  # right child

    # check if left child exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # check if right child exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root again.
        heapify(arr, n, largest)




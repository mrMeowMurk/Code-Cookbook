def heapify(arr, n, i):
    """
    To heapify subtree rooted at index i.
    n is size of heap
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Heap Sort implementation in Python.
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test the heap sort
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    sorted_array = heap_sort(test_array)
    print("Sorted array:", sorted_array) 
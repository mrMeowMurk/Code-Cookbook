def insertion_sort(arr):
    """
    Insertion Sort implementation in Python.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test the insertion sort
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    sorted_array = insertion_sort(test_array)
    print("Sorted array:", sorted_array) 
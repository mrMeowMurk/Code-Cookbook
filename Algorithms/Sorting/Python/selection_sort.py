def selection_sort(arr):
    """
    Selection Sort implementation in Python.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test the selection sort
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    sorted_array = selection_sort(test_array)
    print("Sorted array:", sorted_array) 
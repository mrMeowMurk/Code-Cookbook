def binary_search(arr, target):
    """
    Binary Search implementation in Python.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Note: Array must be sorted
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found
    return -1

# Example usage
if __name__ == "__main__":
    # Test the binary search
    test_array = [11, 12, 22, 25, 34, 64, 90]  # Must be sorted
    target = 25
    
    print("Array:", test_array)
    print("Searching for:", target)
    
    result = binary_search(test_array, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array") 
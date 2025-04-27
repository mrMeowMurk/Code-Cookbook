def linear_search(arr, target):
    """
    Linear Search implementation in Python.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

# Example usage
if __name__ == "__main__":
    # Test the linear search
    test_array = [64, 34, 25, 12, 22, 11, 90]
    target = 25
    
    print("Array:", test_array)
    print("Searching for:", target)
    
    result = linear_search(test_array, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array") 
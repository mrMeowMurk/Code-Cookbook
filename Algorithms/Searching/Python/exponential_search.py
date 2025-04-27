def binary_search(arr, target, left, right):
    """
    Helper function for binary search within a range
    """
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def exponential_search(arr, target):
    """
    Exponential Search implementation in Python.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Note: Array must be sorted
    """
    n = len(arr)
    
    # If array is empty
    if n == 0:
        return -1
    
    # If target is the first element
    if arr[0] == target:
        return 0
    
    # Find range for binary search by repeated doubling
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2
    
    # Call binary search for the found range
    return binary_search(arr, target, i // 2, min(i, n - 1))

# Example usage
if __name__ == "__main__":
    # Test the exponential search
    test_array = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100]  # Must be sorted
    target = 10
    
    print("Array:", test_array)
    print("Searching for:", target)
    
    result = exponential_search(test_array, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array") 
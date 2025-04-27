def interpolation_search(arr, target):
    """
    Interpolation Search implementation in Python.
    Time Complexity: O(log log n) average case, O(n) worst case
    Space Complexity: O(1)
    Note: Array must be sorted and uniformly distributed
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # Probing the position with keeping uniform distribution in mind
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))
        
        # Target found
        if arr[pos] == target:
            return pos
        
        # Target is in upper part
        if arr[pos] < target:
            low = pos + 1
        
        # Target is in lower part
        else:
            high = pos - 1
    
    return -1

# Example usage
if __name__ == "__main__":
    # Test the interpolation search
    test_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Must be sorted and uniformly distributed
    target = 50
    
    print("Array:", test_array)
    print("Searching for:", target)
    
    result = interpolation_search(test_array, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array") 
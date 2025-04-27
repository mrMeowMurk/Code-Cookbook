def fibonacci_search(arr, target):
    """
    Fibonacci Search implementation in Python.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Note: Array must be sorted
    """
    # Initialize Fibonacci numbers
    fib2 = 0  # (k-2)'th Fibonacci number
    fib1 = 1  # (k-1)'th Fibonacci number
    fib = fib1 + fib2  # k'th Fibonacci number
    
    # fib is going to store the smallest Fibonacci
    # number greater than or equal to len(arr)
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    
    # Marks the eliminated range from front
    offset = -1
    
    # While there are elements to be inspected
    while fib > 1:
        # Check if fib2 is a valid location
        i = min(offset + fib2, len(arr) - 1)
        
        # If target is greater than the value at index i,
        # cut the subarray from offset to i
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        
        # If target is less than the value at index i,
        # cut the subarray after i+1
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        
        # Element found
        else:
            return i
    
    # Compare the last element with target
    if fib1 and offset < len(arr) - 1 and arr[offset + 1] == target:
        return offset + 1
    
    # Element not found
    return -1

# Example usage
if __name__ == "__main__":
    # Test the fibonacci search
    test_array = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]  # Must be sorted
    target = 85
    
    print("Array:", test_array)
    print("Searching for:", target)
    
    result = fibonacci_search(test_array, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array") 
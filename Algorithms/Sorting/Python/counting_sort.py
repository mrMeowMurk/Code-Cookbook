def counting_sort(arr):
    """
    Counting Sort implementation in Python.
    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(n + k)
    """
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Create a count array to store count of each element
    count = [0] * (max_element + 1)
    
    # Store count of each element in count array
    for num in arr:
        count[num] += 1
    
    # Change count[i] so that count[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build the output array
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output

# Example usage
if __name__ == "__main__":
    # Test the counting sort
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    sorted_array = counting_sort(test_array)
    print("Sorted array:", sorted_array) 
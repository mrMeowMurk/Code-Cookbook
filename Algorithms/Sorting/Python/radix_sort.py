def counting_sort_for_radix(arr, exp):
    """
    A function to do counting sort of arr[] according to
    the digit represented by exp.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy the output array to arr[], so that arr[] now
    # contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Radix Sort implementation in Python.
    Time Complexity: O(d * (n + k)) where d is the number of digits
    Space Complexity: O(n + k)
    """
    # Find the maximum number to know number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test the radix sort
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    sorted_array = radix_sort(test_array)
    print("Sorted array:", sorted_array) 
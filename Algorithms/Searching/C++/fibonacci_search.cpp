#include <iostream>
#include <vector>

int fibonacciSearch(const std::vector<int>& arr, int target) {
    /**
     * Fibonacci Search implementation in C++.
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     * Note: Array must be sorted
     */
    // Initialize Fibonacci numbers
    int fib2 = 0;  // (k-2)'th Fibonacci number
    int fib1 = 1;  // (k-1)'th Fibonacci number
    int fib = fib1 + fib2;  // k'th Fibonacci number
    
    // fib is going to store the smallest Fibonacci
    // number greater than or equal to arr.size()
    while (fib < arr.size()) {
        fib2 = fib1;
        fib1 = fib;
        fib = fib1 + fib2;
    }
    
    // Marks the eliminated range from front
    int offset = -1;
    
    // While there are elements to be inspected
    while (fib > 1) {
        // Check if fib2 is a valid location
        int i = std::min(offset + fib2, static_cast<int>(arr.size() - 1));
        
        // If target is greater than the value at index i,
        // cut the subarray from offset to i
        if (arr[i] < target) {
            fib = fib1;
            fib1 = fib2;
            fib2 = fib - fib1;
            offset = i;
        }
        // If target is less than the value at index i,
        // cut the subarray after i+1
        else if (arr[i] > target) {
            fib = fib2;
            fib1 = fib1 - fib2;
            fib2 = fib - fib1;
        }
        // Element found
        else {
            return i;
        }
    }
    
    // Compare the last element with target
    if (fib1 && offset < arr.size() - 1 && arr[offset + 1] == target) {
        return offset + 1;
    }
    
    // Element not found
    return -1;
}

int main() {
    // Test the fibonacci search
    std::vector<int> test_array = {10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100};  // Must be sorted
    int target = 85;
    
    std::cout << "Array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    std::cout << "Searching for: " << target << std::endl;
    
    int result = fibonacciSearch(test_array, target);
    if (result != -1) {
        std::cout << "Element found at index: " << result << std::endl;
    } else {
        std::cout << "Element not found in the array" << std::endl;
    }
    
    return 0;
} 
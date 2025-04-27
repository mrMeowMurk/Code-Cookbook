#include <iostream>
#include <vector>

int binarySearch(const std::vector<int>& arr, int target) {
    /**
     * Binary Search implementation in C++.
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     * Note: Array must be sorted
     */
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        // Check if target is present at mid
        if (arr[mid] == target) {
            return mid;
        }
        
        // If target is greater, ignore left half
        if (arr[mid] < target) {
            left = mid + 1;
        }
        // If target is smaller, ignore right half
        else {
            right = mid - 1;
        }
    }
    
    // Target not found
    return -1;
}

int main() {
    // Test the binary search
    std::vector<int> test_array = {11, 12, 22, 25, 34, 64, 90};  // Must be sorted
    int target = 25;
    
    std::cout << "Array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    std::cout << "Searching for: " << target << std::endl;
    
    int result = binarySearch(test_array, target);
    if (result != -1) {
        std::cout << "Element found at index: " << result << std::endl;
    } else {
        std::cout << "Element not found in the array" << std::endl;
    }
    
    return 0;
} 
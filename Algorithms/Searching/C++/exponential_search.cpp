#include <iostream>
#include <vector>

int binarySearch(const std::vector<int>& arr, int target, int left, int right) {
    /**
     * Helper function for binary search within a range
     */
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    
    return -1;
}

int exponentialSearch(const std::vector<int>& arr, int target) {
    /**
     * Exponential Search implementation in C++.
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     * Note: Array must be sorted
     */
    int n = arr.size();
    
    // If array is empty
    if (n == 0) {
        return -1;
    }
    
    // If target is the first element
    if (arr[0] == target) {
        return 0;
    }
    
    // Find range for binary search by repeated doubling
    int i = 1;
    while (i < n && arr[i] <= target) {
        i = i * 2;
    }
    
    // Call binary search for the found range
    return binarySearch(arr, target, i / 2, std::min(i, n - 1));
}

int main() {
    // Test the exponential search
    std::vector<int> test_array = {2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100};  // Must be sorted
    int target = 10;
    
    std::cout << "Array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    std::cout << "Searching for: " << target << std::endl;
    
    int result = exponentialSearch(test_array, target);
    if (result != -1) {
        std::cout << "Element found at index: " << result << std::endl;
    } else {
        std::cout << "Element not found in the array" << std::endl;
    }
    
    return 0;
} 
#include <iostream>
#include <vector>

int linearSearch(const std::vector<int>& arr, int target) {
    /**
     * Linear Search implementation in C++.
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            return i;  // Return the index if found
        }
    }
    return -1;  // Return -1 if not found
}

int main() {
    // Test the linear search
    std::vector<int> test_array = {64, 34, 25, 12, 22, 11, 90};
    int target = 25;
    
    std::cout << "Array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    std::cout << "Searching for: " << target << std::endl;
    
    int result = linearSearch(test_array, target);
    if (result != -1) {
        std::cout << "Element found at index: " << result << std::endl;
    } else {
        std::cout << "Element not found in the array" << std::endl;
    }
    
    return 0;
} 
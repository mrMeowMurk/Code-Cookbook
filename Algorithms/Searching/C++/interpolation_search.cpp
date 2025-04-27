#include <iostream>
#include <vector>

int interpolationSearch(const std::vector<int>& arr, int target) {
    /**
     * Interpolation Search implementation in C++.
     * Time Complexity: O(log log n) average case, O(n) worst case
     * Space Complexity: O(1)
     * Note: Array must be sorted and uniformly distributed
     */
    int low = 0;
    int high = arr.size() - 1;
    
    while (low <= high && target >= arr[low] && target <= arr[high]) {
        if (low == high) {
            if (arr[low] == target) {
                return low;
            }
            return -1;
        }
        
        // Probing the position with keeping uniform distribution in mind
        int pos = low + (((double)(high - low) / (arr[high] - arr[low])) * (target - arr[low]));
        
        // Target found
        if (arr[pos] == target) {
            return pos;
        }
        
        // Target is in upper part
        if (arr[pos] < target) {
            low = pos + 1;
        }
        // Target is in lower part
        else {
            high = pos - 1;
        }
    }
    
    return -1;
}

int main() {
    // Test the interpolation search
    std::vector<int> test_array = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};  // Must be sorted and uniformly distributed
    int target = 50;
    
    std::cout << "Array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    std::cout << "Searching for: " << target << std::endl;
    
    int result = interpolationSearch(test_array, target);
    if (result != -1) {
        std::cout << "Element found at index: " << result << std::endl;
    } else {
        std::cout << "Element not found in the array" << std::endl;
    }
    
    return 0;
} 
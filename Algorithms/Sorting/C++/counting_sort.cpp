#include <iostream>
#include <vector>
#include <algorithm>

void countingSort(std::vector<int>& arr) {
    int n = arr.size();
    
    // Find the maximum element in the array
    int max_element = *std::max_element(arr.begin(), arr.end());
    
    // Create a count array to store count of each element
    std::vector<int> count(max_element + 1, 0);
    
    // Store count of each element in count array
    for (int num : arr) {
        count[num]++;
    }
    
    // Change count[i] so that count[i] now contains actual
    // position of this element in output array
    for (int i = 1; i <= max_element; i++) {
        count[i] += count[i - 1];
    }
    
    // Build the output array
    std::vector<int> output(n);
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }
    
    // Copy the output array to arr[], so that arr[] now
    // contains sorted numbers
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

int main() {
    // Test the counting sort
    std::vector<int> test_array = {64, 34, 25, 12, 22, 11, 90};
    
    std::cout << "Original array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    countingSort(test_array);
    
    std::cout << "Sorted array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
} 
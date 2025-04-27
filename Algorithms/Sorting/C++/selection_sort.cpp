#include <iostream>
#include <vector>

void selectionSort(std::vector<int>& arr) {
    int n = arr.size();
    
    // Traverse through all array elements
    for (int i = 0; i < n-1; i++) {
        // Find the minimum element in remaining unsorted array
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        
        // Swap the found minimum element with the first element
        std::swap(arr[i], arr[min_idx]);
    }
}

int main() {
    // Test the selection sort
    std::vector<int> test_array = {64, 34, 25, 12, 22, 11, 90};
    
    std::cout << "Original array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    selectionSort(test_array);
    
    std::cout << "Sorted array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
} 
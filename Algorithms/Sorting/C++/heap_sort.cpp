#include <iostream>
#include <vector>

void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i;  // Initialize largest as root
    int left = 2 * i + 1;  // left = 2*i + 1
    int right = 2 * i + 2;  // right = 2*i + 2

    // See if left child of root exists and is greater than root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // See if right child of root exists and is greater than root
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // Change root, if needed
    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        // Heapify the root.
        heapify(arr, n, largest);
    }
}

void heapSort(std::vector<int>& arr) {
    int n = arr.size();

    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // One by one extract an element from heap
    for (int i = n - 1; i > 0; i--) {
        // Move current root to end
        std::swap(arr[0], arr[i]);
        // call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}

int main() {
    // Test the heap sort
    std::vector<int> test_array = {64, 34, 25, 12, 22, 11, 90};
    
    std::cout << "Original array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    heapSort(test_array);
    
    std::cout << "Sorted array: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
} 
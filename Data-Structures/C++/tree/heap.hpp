#ifndef HEAP_HPP
#define HEAP_HPP

#include <vector>
#include <stdexcept>
#include <functional>

/**
 * @class Heap
 * @brief A Heap implementation.
 * 
 * A Heap is a specialized tree-based data structure that satisfies the heap property.
 * In a max heap, for any given node N, the value of N is greater than or equal to
 * the values of its children. In a min heap, the value of N is less than or equal to
 * the values of its children.
 */
template<typename T>
class Heap {
private:
    std::vector<T> heap;
    std::function<bool(const T&, const T&)> compare;

    /**
     * @brief Get the index of the parent node.
     * 
     * @param index The index of the current node.
     * @return size_t The index of the parent node.
     */
    size_t parent(size_t index) const {
        return (index - 1) / 2;
    }

    /**
     * @brief Get the index of the left child node.
     * 
     * @param index The index of the current node.
     * @return size_t The index of the left child node.
     */
    size_t left_child(size_t index) const {
        return 2 * index + 1;
    }

    /**
     * @brief Get the index of the right child node.
     * 
     * @param index The index of the current node.
     * @return size_t The index of the right child node.
     */
    size_t right_child(size_t index) const {
        return 2 * index + 2;
    }

    /**
     * @brief Swap two elements in the heap.
     * 
     * @param i The index of the first element.
     * @param j The index of the second element.
     */
    void swap(size_t i, size_t j) {
        std::swap(heap[i], heap[j]);
    }

    /**
     * @brief Heapify the subtree rooted at the given index.
     * 
     * @param index The index of the root of the subtree.
     */
    void heapify(size_t index) {
        size_t largest = index;
        size_t left = left_child(index);
        size_t right = right_child(index);

        if (left < heap.size() && compare(heap[left], heap[largest])) {
            largest = left;
        }

        if (right < heap.size() && compare(heap[right], heap[largest])) {
            largest = right;
        }

        if (largest != index) {
            swap(index, largest);
            heapify(largest);
        }
    }

public:
    /**
     * @brief Constructor.
     * 
     * @param is_max_heap If true, creates a max heap; if false, creates a min heap.
     */
    Heap(bool is_max_heap = true) {
        if (is_max_heap) {
            compare = std::greater<T>();
        } else {
            compare = std::less<T>();
        }
    }

    /**
     * @brief Insert a value into the heap.
     * 
     * @param value The value to insert.
     */
    void insert(const T& value) {
        heap.push_back(value);
        size_t index = heap.size() - 1;

        while (index > 0 && compare(heap[index], heap[parent(index)])) {
            swap(index, parent(index));
            index = parent(index);
        }
    }

    /**
     * @brief Remove and return the root element from the heap.
     * 
     * @return T The root element.
     * @throw std::runtime_error if the heap is empty.
     */
    T extract() {
        if (heap.empty()) {
            throw std::runtime_error("Heap is empty");
        }

        T root = heap[0];
        heap[0] = heap.back();
        heap.pop_back();

        if (!heap.empty()) {
            heapify(0);
        }

        return root;
    }

    /**
     * @brief Return the root element without removing it.
     * 
     * @return T The root element.
     * @throw std::runtime_error if the heap is empty.
     */
    T peek() const {
        if (heap.empty()) {
            throw std::runtime_error("Heap is empty");
        }
        return heap[0];
    }

    /**
     * @brief Check if the heap is empty.
     * 
     * @return true if the heap is empty, false otherwise.
     */
    bool is_empty() const {
        return heap.empty();
    }

    /**
     * @brief Get the number of elements in the heap.
     * 
     * @return size_t The number of elements in the heap.
     */
    size_t size() const {
        return heap.size();
    }

    /**
     * @brief Clear the heap.
     */
    void clear() {
        heap.clear();
    }

    /**
     * @brief Convert the heap to a vector.
     * 
     * @return std::vector<T> A vector containing all elements in the heap.
     */
    std::vector<T> to_vector() const {
        return heap;
    }
};

#endif // HEAP_HPP 
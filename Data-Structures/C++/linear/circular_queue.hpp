#ifndef CIRCULAR_QUEUE_HPP
#define CIRCULAR_QUEUE_HPP

#include <vector>
#include <stdexcept>

/**
 * @class CircularQueue
 * @brief A Circular Queue implementation.
 * 
 * A Circular Queue is a linear data structure that follows the First-In-First-Out (FIFO)
 * principle, but with a fixed size and circular behavior. When the queue is full,
 * new elements can be added by overwriting the oldest elements.
 */
template<typename T>
class CircularQueue {
private:
    std::vector<T> queue;
    size_t front;
    size_t rear;
    size_t size;
    size_t capacity;

public:
    /**
     * @brief Constructor.
     * 
     * @param capacity The maximum number of elements the queue can hold.
     */
    CircularQueue(size_t capacity) : capacity(capacity), front(0), rear(-1), size(0) {
        queue.resize(capacity);
    }

    /**
     * @brief Add an item to the queue.
     * If the queue is full, the oldest item will be overwritten.
     * 
     * @param item The item to be added to the queue.
     */
    void enqueue(const T& item) {
        if (is_full()) {
            // If queue is full, move front pointer to overwrite oldest item
            front = (front + 1) % capacity;
        } else {
            size++;
        }
        
        rear = (rear + 1) % capacity;
        queue[rear] = item;
    }

    /**
     * @brief Remove and return the front item from the queue.
     * 
     * @return T The front item from the queue.
     * @throw std::runtime_error if the queue is empty.
     */
    T dequeue() {
        if (is_empty()) {
            throw std::runtime_error("Queue is empty");
        }
        
        T item = queue[front];
        queue[front] = T();  // Clear the element
        front = (front + 1) % capacity;
        size--;
        
        return item;
    }

    /**
     * @brief Return the front item from the queue without removing it.
     * 
     * @return T The front item from the queue.
     * @throw std::runtime_error if the queue is empty.
     */
    T peek() const {
        if (is_empty()) {
            throw std::runtime_error("Queue is empty");
        }
        return queue[front];
    }

    /**
     * @brief Check if the queue is empty.
     * 
     * @return true if the queue is empty, false otherwise.
     */
    bool is_empty() const {
        return size == 0;
    }

    /**
     * @brief Check if the queue is full.
     * 
     * @return true if the queue is full, false otherwise.
     */
    bool is_full() const {
        return size == capacity;
    }

    /**
     * @brief Get the number of items in the queue.
     * 
     * @return size_t The number of items in the queue.
     */
    size_t get_size() const {
        return size;
    }

    /**
     * @brief Get the capacity of the queue.
     * 
     * @return size_t The capacity of the queue.
     */
    size_t get_capacity() const {
        return capacity;
    }

    /**
     * @brief Clear the queue.
     */
    void clear() {
        queue.clear();
        queue.resize(capacity);
        front = 0;
        rear = -1;
        size = 0;
    }

    /**
     * @brief Convert the queue to a vector.
     * 
     * @return std::vector<T> A vector containing all items in the queue.
     */
    std::vector<T> to_vector() const {
        if (is_empty()) {
            return {};
        }
        
        std::vector<T> result;
        result.reserve(size);
        
        size_t current = front;
        for (size_t i = 0; i < size; i++) {
            result.push_back(queue[current]);
            current = (current + 1) % capacity;
        }
        
        return result;
    }
};

#endif // CIRCULAR_QUEUE_HPP 
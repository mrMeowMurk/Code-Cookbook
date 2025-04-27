/**
 * @file queue.hpp
 * @brief Queue implementation in C++
 * 
 * A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
 * Elements are added at the rear and removed from the front of the queue.
 * 
 * Time Complexity:
 * - Enqueue: O(1)
 * - Dequeue: O(1)
 * - Peek: O(1)
 * - Search: O(n)
 * 
 * Space Complexity: O(n)
 */

#ifndef QUEUE_HPP
#define QUEUE_HPP

#include <deque>
#include <stdexcept>

template<typename T>
class Queue {
private:
    std::deque<T> items;

public:
    /**
     * @brief Default constructor
     */
    Queue() = default;

    /**
     * @brief Add an item to the rear of the queue
     * @param item The item to be added
     */
    void enqueue(const T& item) {
        items.push_back(item);
    }

    /**
     * @brief Remove and return the front item from the queue
     * @return The front item from the queue
     * @throw std::out_of_range if the queue is empty
     */
    T dequeue() {
        if (is_empty()) {
            throw std::out_of_range("Queue is empty");
        }
        T item = items.front();
        items.pop_front();
        return item;
    }

    /**
     * @brief Return the front item from the queue without removing it
     * @return The front item from the queue
     * @throw std::out_of_range if the queue is empty
     */
    T peek() const {
        if (is_empty()) {
            throw std::out_of_range("Queue is empty");
        }
        return items.front();
    }

    /**
     * @brief Check if the queue is empty
     * @return true if the queue is empty, false otherwise
     */
    bool is_empty() const {
        return items.empty();
    }

    /**
     * @brief Return the number of items in the queue
     * @return The number of items in the queue
     */
    size_t size() const {
        return items.size();
    }

    /**
     * @brief Remove all items from the queue
     */
    void clear() {
        items.clear();
    }
};

#endif // QUEUE_HPP 
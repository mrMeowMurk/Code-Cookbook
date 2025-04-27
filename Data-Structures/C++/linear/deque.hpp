#ifndef DEQUE_HPP
#define DEQUE_HPP

#include <vector>
#include <stdexcept>

/**
 * @class Deque
 * @brief A Deque (double-ended queue) implementation.
 * 
 * A Deque is a linear data structure that allows insertion and deletion
 * of elements from both ends. It combines the features of a stack and a queue.
 */
template<typename T>
class Deque {
private:
    std::vector<T> items;

public:
    /**
     * @brief Default constructor.
     */
    Deque() = default;

    /**
     * @brief Add an item to the front of the deque.
     * 
     * @param item The item to be added to the front.
     */
    void add_front(const T& item) {
        items.insert(items.begin(), item);
    }

    /**
     * @brief Add an item to the rear of the deque.
     * 
     * @param item The item to be added to the rear.
     */
    void add_rear(const T& item) {
        items.push_back(item);
    }

    /**
     * @brief Remove and return the front item from the deque.
     * 
     * @return T The front item from the deque.
     * @throw std::runtime_error if the deque is empty.
     */
    T remove_front() {
        if (is_empty()) {
            throw std::runtime_error("Deque is empty");
        }
        T item = items.front();
        items.erase(items.begin());
        return item;
    }

    /**
     * @brief Remove and return the rear item from the deque.
     * 
     * @return T The rear item from the deque.
     * @throw std::runtime_error if the deque is empty.
     */
    T remove_rear() {
        if (is_empty()) {
            throw std::runtime_error("Deque is empty");
        }
        T item = items.back();
        items.pop_back();
        return item;
    }

    /**
     * @brief Return the front item from the deque without removing it.
     * 
     * @return T The front item from the deque.
     * @throw std::runtime_error if the deque is empty.
     */
    T peek_front() const {
        if (is_empty()) {
            throw std::runtime_error("Deque is empty");
        }
        return items.front();
    }

    /**
     * @brief Return the rear item from the deque without removing it.
     * 
     * @return T The rear item from the deque.
     * @throw std::runtime_error if the deque is empty.
     */
    T peek_rear() const {
        if (is_empty()) {
            throw std::runtime_error("Deque is empty");
        }
        return items.back();
    }

    /**
     * @brief Check if the deque is empty.
     * 
     * @return true if the deque is empty, false otherwise.
     */
    bool is_empty() const {
        return items.empty();
    }

    /**
     * @brief Get the number of items in the deque.
     * 
     * @return size_t The number of items in the deque.
     */
    size_t size() const {
        return items.size();
    }

    /**
     * @brief Clear the deque.
     */
    void clear() {
        items.clear();
    }

    /**
     * @brief Convert the deque to a vector.
     * 
     * @return std::vector<T> A vector containing all items in the deque.
     */
    std::vector<T> to_vector() const {
        return items;
    }
};

#endif // DEQUE_HPP 
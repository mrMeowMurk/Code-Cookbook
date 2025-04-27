/**
 * @file stack.hpp
 * @brief Stack implementation in C++
 * 
 * A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
 * Elements are added and removed from the same end, called the top of the stack.
 * 
 * Time Complexity:
 * - Push: O(1)
 * - Pop: O(1)
 * - Peek: O(1)
 * - Search: O(n)
 * 
 * Space Complexity: O(n)
 */

#ifndef STACK_HPP
#define STACK_HPP

#include <vector>
#include <stdexcept>

template<typename T>
class Stack {
private:
    std::vector<T> items;

public:
    /**
     * @brief Default constructor
     */
    Stack() = default;

    /**
     * @brief Add an item to the top of the stack
     * @param item The item to be added
     */
    void push(const T& item) {
        items.push_back(item);
    }

    /**
     * @brief Remove and return the top item from the stack
     * @return The top item from the stack
     * @throw std::out_of_range if the stack is empty
     */
    T pop() {
        if (is_empty()) {
            throw std::out_of_range("Stack is empty");
        }
        T item = items.back();
        items.pop_back();
        return item;
    }

    /**
     * @brief Return the top item from the stack without removing it
     * @return The top item from the stack
     * @throw std::out_of_range if the stack is empty
     */
    T peek() const {
        if (is_empty()) {
            throw std::out_of_range("Stack is empty");
        }
        return items.back();
    }

    /**
     * @brief Check if the stack is empty
     * @return true if the stack is empty, false otherwise
     */
    bool is_empty() const {
        return items.empty();
    }

    /**
     * @brief Return the number of items in the stack
     * @return The number of items in the stack
     */
    size_t size() const {
        return items.size();
    }

    /**
     * @brief Remove all items from the stack
     */
    void clear() {
        items.clear();
    }
};

#endif // STACK_HPP 
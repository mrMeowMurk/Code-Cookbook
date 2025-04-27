#include <iostream>
#include <vector>
#include <stdexcept>

/**
 * @class Stack
 * @brief A simple implementation of a Stack data structure.
 * 
 * A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
 * Elements are added and removed from the same end (top) of the stack.
 */
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
     * @brief Get the number of items in the stack
     * @return The number of items in the stack
     */
    size_t size() const {
        return items.size();
    }

    /**
     * @brief Print the stack contents
     */
    void print() const {
        std::cout << "Stack: [";
        for (size_t i = 0; i < items.size(); ++i) {
            std::cout << items[i];
            if (i < items.size() - 1) {
                std::cout << ", ";
            }
        }
        std::cout << "]" << std::endl;
    }
};

// Example usage
int main() {
    try {
        // Create a new stack
        Stack<int> stack;

        // Push some items
        stack.push(1);
        stack.push(2);
        stack.push(3);

        // Print stack information
        stack.print();
        std::cout << "Size: " << stack.size() << std::endl;
        std::cout << "Top item: " << stack.peek() << std::endl;

        // Pop items
        std::cout << "Popped: " << stack.pop() << std::endl;
        std::cout << "Popped: " << stack.pop() << std::endl;
        stack.print();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
} 
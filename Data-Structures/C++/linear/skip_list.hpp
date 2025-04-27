#ifndef SKIP_LIST_HPP
#define SKIP_LIST_HPP

#include <vector>
#include <random>
#include <limits>
#include <memory>

/**
 * @class SkipListNode
 * @brief A node in the Skip List data structure.
 * 
 * Each node contains a value and a vector of forward pointers.
 */
template<typename T>
class SkipListNode {
public:
    T value;
    std::vector<std::shared_ptr<SkipListNode<T>>> forward;

    SkipListNode(T val, int level) : value(val), forward(level, nullptr) {}
};

/**
 * @class SkipList
 * @brief A Skip List implementation.
 * 
 * A Skip List is a probabilistic data structure that allows for efficient
 * search, insertion, and deletion operations with O(log n) average time complexity.
 */
template<typename T>
class SkipList {
private:
    std::shared_ptr<SkipListNode<T>> header;
    int max_level;
    int level;
    float p;
    std::mt19937 rng;
    std::uniform_real_distribution<float> dist;

    /**
     * @brief Generate a random level for a new node.
     * 
     * @return int A random level between 1 and max_level.
     */
    int random_level() {
        int level = 1;
        while (dist(rng) < p && level < max_level) {
            level++;
        }
        return level;
    }

public:
    /**
     * @brief Constructor.
     * 
     * @param max_level Maximum number of levels in the skip list.
     * @param p Probability of a node being promoted to the next level.
     */
    SkipList(int max_level = 16, float p = 0.5)
        : max_level(max_level), level(0), p(p),
          rng(std::random_device{}()),
          dist(0.0f, 1.0f) {
        header = std::make_shared<SkipListNode<T>>(T(), max_level);
    }

    /**
     * @brief Search for a value in the Skip List.
     * 
     * @param value The value to search for.
     * @return true if the value exists in the Skip List, false otherwise.
     */
    bool search(T value) const {
        auto current = header;
        for (int i = level - 1; i >= 0; i--) {
            while (current->forward[i] && current->forward[i]->value < value) {
                current = current->forward[i];
            }
        }
        current = current->forward[0];
        return current != nullptr && current->value == value;
    }

    /**
     * @brief Insert a value into the Skip List.
     * 
     * @param value The value to insert.
     */
    void insert(T value) {
        std::vector<std::shared_ptr<SkipListNode<T>>> update(max_level, nullptr);
        auto current = header;

        // Find the position to insert
        for (int i = level - 1; i >= 0; i--) {
            while (current->forward[i] && current->forward[i]->value < value) {
                current = current->forward[i];
            }
            update[i] = current;
        }

        current = current->forward[0];

        // If value already exists, don't insert
        if (current != nullptr && current->value == value) {
            return;
        }

        // Generate random level for new node
        int new_level = random_level();

        // Update max level if necessary
        if (new_level > level) {
            for (int i = level; i < new_level; i++) {
                update[i] = header;
            }
            level = new_level;
        }

        // Create new node
        auto new_node = std::make_shared<SkipListNode<T>>(value, new_level);

        // Update forward pointers
        for (int i = 0; i < new_level; i++) {
            new_node->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = new_node;
        }
    }

    /**
     * @brief Delete a value from the Skip List.
     * 
     * @param value The value to delete.
     * @return true if the value was deleted, false if it didn't exist.
     */
    bool remove(T value) {
        std::vector<std::shared_ptr<SkipListNode<T>>> update(max_level, nullptr);
        auto current = header;

        // Find the position to delete
        for (int i = level - 1; i >= 0; i--) {
            while (current->forward[i] && current->forward[i]->value < value) {
                current = current->forward[i];
            }
            update[i] = current;
        }

        current = current->forward[0];

        // If value doesn't exist, return false
        if (current == nullptr || current->value != value) {
            return false;
        }

        // Update forward pointers
        for (int i = 0; i < level; i++) {
            if (update[i]->forward[i] != current) {
                break;
            }
            update[i]->forward[i] = current->forward[i];
        }

        // Update max level if necessary
        while (level > 0 && header->forward[level - 1] == nullptr) {
            level--;
        }

        return true;
    }

    /**
     * @brief Get all values in the Skip List within a given range.
     * 
     * @param start The start of the range (inclusive).
     * @param end The end of the range (inclusive).
     * @return std::vector<T> A vector of values within the range.
     */
    std::vector<T> get_range(T start, T end) const {
        std::vector<T> result;
        auto current = header;

        // Find the first node in the range
        for (int i = level - 1; i >= 0; i--) {
            while (current->forward[i] && current->forward[i]->value < start) {
                current = current->forward[i];
            }
        }

        current = current->forward[0];

        // Collect all values in the range
        while (current && current->value <= end) {
            result.push_back(current->value);
            current = current->forward[0];
        }

        return result;
    }

    /**
     * @brief Print the Skip List.
     */
    void print() const {
        for (int i = level - 1; i >= 0; i--) {
            std::cout << "Level " << i << ": ";
            auto current = header;
            while (current) {
                std::cout << current->value << " -> ";
                current = current->forward[i];
            }
            std::cout << "nullptr" << std::endl;
        }
    }
};

#endif // SKIP_LIST_HPP 
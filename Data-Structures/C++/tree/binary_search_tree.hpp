/**
 * @file binary_search_tree.hpp
 * @brief Binary Search Tree implementation in C++
 * 
 * A binary search tree is a binary tree where each node has a value greater than all values
 * in its left subtree and less than all values in its right subtree.
 * 
 * Time Complexity:
 * - Insert: O(log n) average case, O(n) worst case
 * - Delete: O(log n) average case, O(n) worst case
 * - Search: O(log n) average case, O(n) worst case
 * - Traversal: O(n)
 * 
 * Space Complexity: O(n)
 */

#ifndef BINARY_SEARCH_TREE_HPP
#define BINARY_SEARCH_TREE_HPP

#include <queue>
#include <vector>
#include <stdexcept>
#include <functional>

template<typename T>
class Node {
public:
    T data;
    Node* left;
    Node* right;
    
    Node(const T& data) : data(data), left(nullptr), right(nullptr) {}
};

template<typename T>
class BinarySearchTree {
private:
    Node<T>* root;

public:
    /**
     * @brief Default constructor
     */
    BinarySearchTree() : root(nullptr) {}

    /**
     * @brief Destructor
     */
    ~BinarySearchTree() {
        clear();
    }

    /**
     * @brief Check if the binary search tree is empty
     * @return true if the binary search tree is empty, false otherwise
     */
    bool is_empty() const {
        return root == nullptr;
    }

    /**
     * @brief Insert a new node into the binary search tree
     * @param data The data to be inserted
     */
    void insert(const T& data) {
        if (is_empty()) {
            root = new Node<T>(data);
            return;
        }

        Node<T>* current = root;
        while (true) {
            if (data < current->data) {
                if (current->left == nullptr) {
                    current->left = new Node<T>(data);
                    return;
                }
                current = current->left;
            } else {
                if (current->right == nullptr) {
                    current->right = new Node<T>(data);
                    return;
                }
                current = current->right;
            }
        }
    }

    /**
     * @brief Delete a node with the given data from the binary search tree
     * @param data The data to be deleted
     * @return true if the node was deleted, false otherwise
     */
    bool delete_node(const T& data) {
        if (is_empty()) {
            return false;
        }

        // Find the node to be deleted and its parent
        Node<T>* current = root;
        Node<T>* parent = nullptr;
        bool is_left_child = false;

        while (current && current->data != data) {
            parent = current;
            if (data < current->data) {
                current = current->left;
                is_left_child = true;
            } else {
                current = current->right;
                is_left_child = false;
            }
        }

        if (current == nullptr) {
            return false;
        }

        // Case 1: Node to be deleted is a leaf node
        if (current->left == nullptr && current->right == nullptr) {
            if (parent == nullptr) {
                root = nullptr;
            } else if (is_left_child) {
                parent->left = nullptr;
            } else {
                parent->right = nullptr;
            }
            delete current;
            return true;
        }

        // Case 2: Node to be deleted has only one child
        if (current->left == nullptr) {
            if (parent == nullptr) {
                root = current->right;
            } else if (is_left_child) {
                parent->left = current->right;
            } else {
                parent->right = current->right;
            }
            delete current;
            return true;
        }

        if (current->right == nullptr) {
            if (parent == nullptr) {
                root = current->left;
            } else if (is_left_child) {
                parent->left = current->left;
            } else {
                parent->right = current->left;
            }
            delete current;
            return true;
        }

        // Case 3: Node to be deleted has two children
        // Find the inorder successor (smallest node in the right subtree)
        Node<T>* successor = current->right;
        Node<T>* successor_parent = current;
        bool is_successor_left_child = false;

        while (successor->left) {
            successor_parent = successor;
            successor = successor->left;
            is_successor_left_child = true;
        }

        // Replace the node to be deleted with its successor
        current->data = successor->data;

        // Delete the successor
        if (is_successor_left_child) {
            successor_parent->left = successor->right;
        } else {
            successor_parent->right = successor->right;
        }
        delete successor;
        return true;
    }

    /**
     * @brief Search for a node with the given data in the binary search tree
     * @param data The data to search for
     * @return true if the node is found, false otherwise
     */
    bool search(const T& data) const {
        if (is_empty()) {
            return false;
        }

        Node<T>* current = root;
        while (current) {
            if (data == current->data) {
                return true;
            }
            if (data < current->data) {
                current = current->left;
            } else {
                current = current->right;
            }
        }

        return false;
    }

    /**
     * @brief Perform an inorder traversal of the binary search tree
     * @return A vector containing the nodes in inorder traversal order
     */
    std::vector<T> inorder_traversal() const {
        std::vector<T> result;
        
        std::function<void(Node<T>*)> inorder = [&](Node<T>* node) {
            if (node) {
                inorder(node->left);
                result.push_back(node->data);
                inorder(node->right);
            }
        };
        
        inorder(root);
        return result;
    }

    /**
     * @brief Perform a preorder traversal of the binary search tree
     * @return A vector containing the nodes in preorder traversal order
     */
    std::vector<T> preorder_traversal() const {
        std::vector<T> result;
        
        std::function<void(Node<T>*)> preorder = [&](Node<T>* node) {
            if (node) {
                result.push_back(node->data);
                preorder(node->left);
                preorder(node->right);
            }
        };
        
        preorder(root);
        return result;
    }

    /**
     * @brief Perform a postorder traversal of the binary search tree
     * @return A vector containing the nodes in postorder traversal order
     */
    std::vector<T> postorder_traversal() const {
        std::vector<T> result;
        
        std::function<void(Node<T>*)> postorder = [&](Node<T>* node) {
            if (node) {
                postorder(node->left);
                postorder(node->right);
                result.push_back(node->data);
            }
        };
        
        postorder(root);
        return result;
    }

    /**
     * @brief Get the minimum value in the binary search tree
     * @return The minimum value in the binary search tree
     * @throw std::runtime_error if the binary search tree is empty
     */
    T get_min() const {
        if (is_empty()) {
            throw std::runtime_error("Binary search tree is empty");
        }

        Node<T>* current = root;
        while (current->left) {
            current = current->left;
        }

        return current->data;
    }

    /**
     * @brief Get the maximum value in the binary search tree
     * @return The maximum value in the binary search tree
     * @throw std::runtime_error if the binary search tree is empty
     */
    T get_max() const {
        if (is_empty()) {
            throw std::runtime_error("Binary search tree is empty");
        }

        Node<T>* current = root;
        while (current->right) {
            current = current->right;
        }

        return current->data;
    }

    /**
     * @brief Get the height of the binary search tree
     * @return The height of the binary search tree
     */
    int get_height() const {
        std::function<int(Node<T>*)> height = [&](Node<T>* node) {
            if (node == nullptr) {
                return 0;
            }
            return std::max(height(node->left), height(node->right)) + 1;
        };
        
        return height(root);
    }

    /**
     * @brief Remove all nodes from the binary search tree
     */
    void clear() {
        std::function<void(Node<T>*)> clear_recursive = [&](Node<T>* node) {
            if (node) {
                clear_recursive(node->left);
                clear_recursive(node->right);
                delete node;
            }
        };
        
        clear_recursive(root);
        root = nullptr;
    }
};

#endif // BINARY_SEARCH_TREE_HPP 
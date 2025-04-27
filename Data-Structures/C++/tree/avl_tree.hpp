/**
 * @file avl_tree.hpp
 * @brief AVL Tree implementation in C++
 * 
 * An AVL tree is a self-balancing binary search tree where the heights of the left and right
 * subtrees of any node differ by at most one.
 * 
 * Time Complexity:
 * - Insert: O(log n)
 * - Delete: O(log n)
 * - Search: O(log n)
 * - Traversal: O(n)
 * 
 * Space Complexity: O(n)
 */

#ifndef AVL_TREE_HPP
#define AVL_TREE_HPP

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
    int height;
    
    Node(const T& data) : data(data), left(nullptr), right(nullptr), height(1) {}
};

template<typename T>
class AVLTree {
private:
    Node<T>* root;

    int get_height(Node<T>* node) const {
        if (node == nullptr) {
            return 0;
        }
        return node->height;
    }

    int get_balance(Node<T>* node) const {
        if (node == nullptr) {
            return 0;
        }
        return get_height(node->left) - get_height(node->right);
    }

    Node<T>* right_rotate(Node<T>* y) {
        Node<T>* x = y->left;
        Node<T>* T2 = x->right;

        x->right = y;
        y->left = T2;

        y->height = std::max(get_height(y->left), get_height(y->right)) + 1;
        x->height = std::max(get_height(x->left), get_height(x->right)) + 1;

        return x;
    }

    Node<T>* left_rotate(Node<T>* x) {
        Node<T>* y = x->right;
        Node<T>* T2 = y->left;

        y->left = x;
        x->right = T2;

        x->height = std::max(get_height(x->left), get_height(x->right)) + 1;
        y->height = std::max(get_height(y->left), get_height(y->right)) + 1;

        return y;
    }

    Node<T>* insert_recursive(Node<T>* node, const T& data) {
        if (node == nullptr) {
            return new Node<T>(data);
        }

        if (data < node->data) {
            node->left = insert_recursive(node->left, data);
        } else {
            node->right = insert_recursive(node->right, data);
        }

        node->height = std::max(get_height(node->left), get_height(node->right)) + 1;

        int balance = get_balance(node);

        // Left Left Case
        if (balance > 1 && data < node->left->data) {
            return right_rotate(node);
        }

        // Right Right Case
        if (balance < -1 && data > node->right->data) {
            return left_rotate(node);
        }

        // Left Right Case
        if (balance > 1 && data > node->left->data) {
            node->left = left_rotate(node->left);
            return right_rotate(node);
        }

        // Right Left Case
        if (balance < -1 && data < node->right->data) {
            node->right = right_rotate(node->right);
            return left_rotate(node);
        }

        return node;
    }

    Node<T>* delete_recursive(Node<T>* node, const T& data) {
        if (node == nullptr) {
            return nullptr;
        }

        if (data < node->data) {
            node->left = delete_recursive(node->left, data);
        } else if (data > node->data) {
            node->right = delete_recursive(node->right, data);
        } else {
            if (node->left == nullptr) {
                Node<T>* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr) {
                Node<T>* temp = node->left;
                delete node;
                return temp;
            }

            // Node with two children: Get the inorder successor
            Node<T>* temp = node->right;
            while (temp->left) {
                temp = temp->left;
            }

            node->data = temp->data;
            node->right = delete_recursive(node->right, temp->data);
        }

        if (node == nullptr) {
            return nullptr;
        }

        node->height = std::max(get_height(node->left), get_height(node->right)) + 1;

        int balance = get_balance(node);

        // Left Left Case
        if (balance > 1 && get_balance(node->left) >= 0) {
            return right_rotate(node);
        }

        // Left Right Case
        if (balance > 1 && get_balance(node->left) < 0) {
            node->left = left_rotate(node->left);
            return right_rotate(node);
        }

        // Right Right Case
        if (balance < -1 && get_balance(node->right) <= 0) {
            return left_rotate(node);
        }

        // Right Left Case
        if (balance < -1 && get_balance(node->right) > 0) {
            node->right = right_rotate(node->right);
            return left_rotate(node);
        }

        return node;
    }

    bool search_recursive(Node<T>* node, const T& data) const {
        if (node == nullptr) {
            return false;
        }

        if (data == node->data) {
            return true;
        } else if (data < node->data) {
            return search_recursive(node->left, data);
        } else {
            return search_recursive(node->right, data);
        }
    }

    void clear_recursive(Node<T>* node) {
        if (node) {
            clear_recursive(node->left);
            clear_recursive(node->right);
            delete node;
        }
    }

public:
    /**
     * @brief Default constructor
     */
    AVLTree() : root(nullptr) {}

    /**
     * @brief Destructor
     */
    ~AVLTree() {
        clear();
    }

    /**
     * @brief Check if the AVL tree is empty
     * @return true if the AVL tree is empty, false otherwise
     */
    bool is_empty() const {
        return root == nullptr;
    }

    /**
     * @brief Insert a new node into the AVL tree
     * @param data The data to be inserted
     */
    void insert(const T& data) {
        root = insert_recursive(root, data);
    }

    /**
     * @brief Delete a node with the given data from the AVL tree
     * @param data The data to be deleted
     * @return true if the node was deleted, false otherwise
     */
    bool delete_node(const T& data) {
        if (is_empty()) {
            return false;
        }

        root = delete_recursive(root, data);
        return true;
    }

    /**
     * @brief Search for a node with the given data in the AVL tree
     * @param data The data to search for
     * @return true if the node is found, false otherwise
     */
    bool search(const T& data) const {
        return search_recursive(root, data);
    }

    /**
     * @brief Perform an inorder traversal of the AVL tree
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
     * @brief Perform a preorder traversal of the AVL tree
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
     * @brief Perform a postorder traversal of the AVL tree
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
     * @brief Get the minimum value in the AVL tree
     * @return The minimum value in the AVL tree
     * @throw std::runtime_error if the AVL tree is empty
     */
    T get_min() const {
        if (is_empty()) {
            throw std::runtime_error("AVL tree is empty");
        }

        Node<T>* current = root;
        while (current->left) {
            current = current->left;
        }

        return current->data;
    }

    /**
     * @brief Get the maximum value in the AVL tree
     * @return The maximum value in the AVL tree
     * @throw std::runtime_error if the AVL tree is empty
     */
    T get_max() const {
        if (is_empty()) {
            throw std::runtime_error("AVL tree is empty");
        }

        Node<T>* current = root;
        while (current->right) {
            current = current->right;
        }

        return current->data;
    }

    /**
     * @brief Remove all nodes from the AVL tree
     */
    void clear() {
        clear_recursive(root);
        root = nullptr;
    }
};

#endif // AVL_TREE_HPP 
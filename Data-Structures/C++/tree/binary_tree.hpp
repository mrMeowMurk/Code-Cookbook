/**
 * @file binary_tree.hpp
 * @brief Binary Tree implementation in C++
 * 
 * A binary tree is a tree data structure in which each node has at most two children,
 * referred to as the left child and the right child.
 * 
 * Time Complexity:
 * - Insert: O(n) in worst case
 * - Delete: O(n) in worst case
 * - Search: O(n) in worst case
 * - Traversal: O(n)
 * 
 * Space Complexity: O(n)
 */

#ifndef BINARY_TREE_HPP
#define BINARY_TREE_HPP

#include <queue>
#include <vector>
#include <stdexcept>

template<typename T>
class Node {
public:
    T data;
    Node* left;
    Node* right;
    
    Node(const T& data) : data(data), left(nullptr), right(nullptr) {}
};

template<typename T>
class BinaryTree {
private:
    Node<T>* root;

public:
    /**
     * @brief Default constructor
     */
    BinaryTree() : root(nullptr) {}

    /**
     * @brief Destructor
     */
    ~BinaryTree() {
        clear();
    }

    /**
     * @brief Check if the binary tree is empty
     * @return true if the binary tree is empty, false otherwise
     */
    bool is_empty() const {
        return root == nullptr;
    }

    /**
     * @brief Insert a new node into the binary tree
     * @param data The data to be inserted
     */
    void insert(const T& data) {
        if (is_empty()) {
            root = new Node<T>(data);
            return;
        }

        std::queue<Node<T>*> queue;
        queue.push(root);

        while (!queue.empty()) {
            Node<T>* node = queue.front();
            queue.pop();

            if (node->left == nullptr) {
                node->left = new Node<T>(data);
                return;
            }
            queue.push(node->left);

            if (node->right == nullptr) {
                node->right = new Node<T>(data);
                return;
            }
            queue.push(node->right);
        }
    }

    /**
     * @brief Delete a node with the given data from the binary tree
     * @param data The data to be deleted
     * @return true if the node was deleted, false otherwise
     */
    bool delete_node(const T& data) {
        if (is_empty()) {
            return false;
        }

        // Find the node to be deleted and its parent
        Node<T>* node_to_delete = nullptr;
        Node<T>* parent = nullptr;
        std::queue<std::pair<Node<T>*, Node<T>*>> queue;
        queue.push({root, nullptr});

        while (!queue.empty()) {
            auto [node, parent_node] = queue.front();
            queue.pop();

            if (node->data == data) {
                node_to_delete = node;
                parent = parent_node;
                break;
            }

            if (node->left) {
                queue.push({node->left, node});
            }
            if (node->right) {
                queue.push({node->right, node});
            }
        }

        if (node_to_delete == nullptr) {
            return false;
        }

        // If the node to be deleted is a leaf node
        if (node_to_delete->left == nullptr && node_to_delete->right == nullptr) {
            if (parent == nullptr) {
                root = nullptr;
            } else if (parent->left == node_to_delete) {
                parent->left = nullptr;
            } else {
                parent->right = nullptr;
            }
            delete node_to_delete;
            return true;
        }

        // If the node to be deleted has only one child
        if (node_to_delete->left == nullptr) {
            if (parent == nullptr) {
                root = node_to_delete->right;
            } else if (parent->left == node_to_delete) {
                parent->left = node_to_delete->right;
            } else {
                parent->right = node_to_delete->right;
            }
            delete node_to_delete;
            return true;
        }

        if (node_to_delete->right == nullptr) {
            if (parent == nullptr) {
                root = node_to_delete->left;
            } else if (parent->left == node_to_delete) {
                parent->left = node_to_delete->left;
            } else {
                parent->right = node_to_delete->left;
            }
            delete node_to_delete;
            return true;
        }

        // If the node to be deleted has two children
        // Find the inorder successor (smallest node in the right subtree)
        Node<T>* successor = node_to_delete->right;
        Node<T>* successor_parent = node_to_delete;

        while (successor->left) {
            successor_parent = successor;
            successor = successor->left;
        }

        // Replace the node to be deleted with its successor
        node_to_delete->data = successor->data;

        // Delete the successor
        if (successor_parent->left == successor) {
            successor_parent->left = successor->right;
        } else {
            successor_parent->right = successor->right;
        }
        delete successor;
        return true;
    }

    /**
     * @brief Search for a node with the given data in the binary tree
     * @param data The data to search for
     * @return true if the node is found, false otherwise
     */
    bool search(const T& data) const {
        if (is_empty()) {
            return false;
        }

        std::queue<Node<T>*> queue;
        queue.push(root);

        while (!queue.empty()) {
            Node<T>* node = queue.front();
            queue.pop();

            if (node->data == data) {
                return true;
            }

            if (node->left) {
                queue.push(node->left);
            }
            if (node->right) {
                queue.push(node->right);
            }
        }

        return false;
    }

    /**
     * @brief Perform an inorder traversal of the binary tree
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
     * @brief Perform a preorder traversal of the binary tree
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
     * @brief Perform a postorder traversal of the binary tree
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
     * @brief Perform a level order traversal of the binary tree
     * @return A vector containing the nodes in level order traversal order
     */
    std::vector<T> level_order_traversal() const {
        if (is_empty()) {
            return {};
        }

        std::vector<T> result;
        std::queue<Node<T>*> queue;
        queue.push(root);

        while (!queue.empty()) {
            Node<T>* node = queue.front();
            queue.pop();
            result.push_back(node->data);

            if (node->left) {
                queue.push(node->left);
            }
            if (node->right) {
                queue.push(node->right);
            }
        }

        return result;
    }

    /**
     * @brief Get the height of the binary tree
     * @return The height of the binary tree
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
     * @brief Remove all nodes from the binary tree
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

#endif // BINARY_TREE_HPP 
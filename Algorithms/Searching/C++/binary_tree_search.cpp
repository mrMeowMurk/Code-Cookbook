#include <iostream>

class Node {
public:
    int key;
    Node* left;
    Node* right;
    
    Node(int value) : key(value), left(nullptr), right(nullptr) {}
};

class BinarySearchTree {
private:
    Node* root;
    
    Node* insertRecursive(Node* node, int key) {
        if (node == nullptr) {
            return new Node(key);
        }
        
        if (key < node->key) {
            node->left = insertRecursive(node->left, key);
        }
        else if (key > node->key) {
            node->right = insertRecursive(node->right, key);
        }
        
        return node;
    }
    
    Node* searchRecursive(Node* node, int key) {
        // Base cases: root is null or key is present at root
        if (node == nullptr || node->key == key) {
            return node;
        }
        
        // Key is greater than root's key
        if (key > node->key) {
            return searchRecursive(node->right, key);
        }
        
        // Key is smaller than root's key
        return searchRecursive(node->left, key);
    }
    
public:
    BinarySearchTree() : root(nullptr) {}
    
    void insert(int key) {
        root = insertRecursive(root, key);
    }
    
    Node* search(int key) {
        return searchRecursive(root, key);
    }
};

int main() {
    // Create a BST
    BinarySearchTree bst;
    
    // Insert some keys
    int keys[] = {50, 30, 70, 20, 40, 60, 80};
    for (int key : keys) {
        bst.insert(key);
    }
    
    // Search for keys
    int searchKeys[] = {40, 90, 20};
    for (int key : searchKeys) {
        Node* result = bst.search(key);
        if (result) {
            std::cout << "Key " << key << " found in the BST" << std::endl;
        } else {
            std::cout << "Key " << key << " not found in the BST" << std::endl;
        }
    }
    
    return 0;
} 
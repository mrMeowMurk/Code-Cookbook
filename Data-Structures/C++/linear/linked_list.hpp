/**
 * @file linked_list.hpp
 * @brief Singly Linked List implementation in C++
 * 
 * A linked list is a linear data structure where each element is a separate object called a node.
 * Each node contains data and a reference to the next node in the sequence.
 * 
 * Time Complexity:
 * - Insert at beginning: O(1)
 * - Insert at end: O(n)
 * - Insert at position: O(n)
 * - Delete at beginning: O(1)
 * - Delete at end: O(n)
 * - Delete at position: O(n)
 * - Search: O(n)
 * - Access: O(n)
 * 
 * Space Complexity: O(n)
 */

#ifndef LINKED_LIST_HPP
#define LINKED_LIST_HPP

#include <stdexcept>
#include <string>
#include <sstream>

template<typename T>
class Node {
public:
    T data;
    Node* next;
    
    Node(const T& data) : data(data), next(nullptr) {}
};

template<typename T>
class LinkedList {
private:
    Node<T>* head;
    size_t size;

public:
    /**
     * @brief Default constructor
     */
    LinkedList() : head(nullptr), size(0) {}

    /**
     * @brief Destructor
     */
    ~LinkedList() {
        clear();
    }

    /**
     * @brief Check if the linked list is empty
     * @return true if the linked list is empty, false otherwise
     */
    bool is_empty() const {
        return head == nullptr;
    }

    /**
     * @brief Insert a new node at the beginning of the linked list
     * @param data The data to be inserted
     */
    void insert_at_beginning(const T& data) {
        Node<T>* new_node = new Node<T>(data);
        new_node->next = head;
        head = new_node;
        size++;
    }

    /**
     * @brief Insert a new node at the end of the linked list
     * @param data The data to be inserted
     */
    void insert_at_end(const T& data) {
        Node<T>* new_node = new Node<T>(data);
        
        if (is_empty()) {
            head = new_node;
        } else {
            Node<T>* current = head;
            while (current->next) {
                current = current->next;
            }
            current->next = new_node;
        }
        
        size++;
    }

    /**
     * @brief Insert a new node at the specified position
     * @param data The data to be inserted
     * @param position The position where the node should be inserted (0-based)
     * @throw std::out_of_range if the position is invalid
     */
    void insert_at_position(const T& data, size_t position) {
        if (position > size) {
            throw std::out_of_range("Invalid position");
        }
        
        if (position == 0) {
            insert_at_beginning(data);
            return;
        }
        
        Node<T>* new_node = new Node<T>(data);
        Node<T>* current = head;
        
        for (size_t i = 0; i < position - 1; i++) {
            current = current->next;
        }
        
        new_node->next = current->next;
        current->next = new_node;
        size++;
    }

    /**
     * @brief Delete the first node from the linked list
     * @throw std::out_of_range if the linked list is empty
     */
    void delete_at_beginning() {
        if (is_empty()) {
            throw std::out_of_range("Linked list is empty");
        }
        
        Node<T>* temp = head;
        head = head->next;
        delete temp;
        size--;
    }

    /**
     * @brief Delete the last node from the linked list
     * @throw std::out_of_range if the linked list is empty
     */
    void delete_at_end() {
        if (is_empty()) {
            throw std::out_of_range("Linked list is empty");
        }
        
        if (size == 1) {
            delete head;
            head = nullptr;
        } else {
            Node<T>* current = head;
            while (current->next->next) {
                current = current->next;
            }
            delete current->next;
            current->next = nullptr;
        }
        
        size--;
    }

    /**
     * @brief Delete the node at the specified position
     * @param position The position of the node to be deleted (0-based)
     * @throw std::out_of_range if the position is invalid or the linked list is empty
     */
    void delete_at_position(size_t position) {
        if (is_empty()) {
            throw std::out_of_range("Linked list is empty");
        }
        
        if (position >= size) {
            throw std::out_of_range("Invalid position");
        }
        
        if (position == 0) {
            delete_at_beginning();
            return;
        }
        
        Node<T>* current = head;
        for (size_t i = 0; i < position - 1; i++) {
            current = current->next;
        }
        
        Node<T>* temp = current->next;
        current->next = temp->next;
        delete temp;
        size--;
    }

    /**
     * @brief Search for a node with the given data
     * @param data The data to search for
     * @return The position of the node if found, -1 otherwise
     */
    int search(const T& data) const {
        Node<T>* current = head;
        int position = 0;
        
        while (current) {
            if (current->data == data) {
                return position;
            }
            current = current->next;
            position++;
        }
        
        return -1;
    }

    /**
     * @brief Return the number of nodes in the linked list
     * @return The number of nodes in the linked list
     */
    size_t get_size() const {
        return size;
    }

    /**
     * @brief Remove all nodes from the linked list
     */
    void clear() {
        while (!is_empty()) {
            delete_at_beginning();
        }
    }

    /**
     * @brief Return a string representation of the linked list
     * @return A string representation of the linked list
     */
    std::string to_string() const {
        if (is_empty()) {
            return "Empty linked list";
        }
        
        std::stringstream ss;
        Node<T>* current = head;
        
        while (current) {
            ss << current->data;
            if (current->next) {
                ss << " -> ";
            }
            current = current->next;
        }
        
        return ss.str();
    }
};

#endif // LINKED_LIST_HPP 
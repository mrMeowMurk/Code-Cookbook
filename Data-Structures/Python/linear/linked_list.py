"""
Singly Linked List Implementation in Python

A linked list is a linear data structure where each element is a separate object called a node.
Each node contains data and a reference to the next node in the sequence.

Time Complexity:
- Insert at beginning: O(1)
- Insert at end: O(n)
- Insert at position: O(n)
- Delete at beginning: O(1)
- Delete at end: O(n)
- Delete at position: O(n)
- Search: O(n)
- Access: O(n)

Space Complexity: O(n)
"""

class Node:
    def __init__(self, data):
        """
        Initialize a new node.
        
        Args:
            data: The data to be stored in the node
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.size = 0

    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
            True if the linked list is empty, False otherwise
        """
        return self.head is None

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the linked list.
        
        Args:
            data: The data to be inserted
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the linked list.
        
        Args:
            data: The data to be inserted
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1

    def insert_at_position(self, data, position):
        """
        Insert a new node at the specified position.
        
        Args:
            data: The data to be inserted
            position: The position where the node should be inserted (0-based)
            
        Raises:
            IndexError: If the position is invalid
        """
        if position < 0 or position > self.size:
            raise IndexError("Invalid position")
            
        if position == 0:
            self.insert_at_beginning(data)
            return
            
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
            
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete_at_beginning(self):
        """
        Delete the first node from the linked list.
        
        Raises:
            IndexError: If the linked list is empty
        """
        if self.is_empty():
            raise IndexError("Linked list is empty")
            
        self.head = self.head.next
        self.size -= 1

    def delete_at_end(self):
        """
        Delete the last node from the linked list.
        
        Raises:
            IndexError: If the linked list is empty
        """
        if self.is_empty():
            raise IndexError("Linked list is empty")
            
        if self.size == 1:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
            
        self.size -= 1

    def delete_at_position(self, position):
        """
        Delete the node at the specified position.
        
        Args:
            position: The position of the node to be deleted (0-based)
            
        Raises:
            IndexError: If the position is invalid or the linked list is empty
        """
        if self.is_empty():
            raise IndexError("Linked list is empty")
            
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
            
        if position == 0:
            self.delete_at_beginning()
            return
            
        current = self.head
        for _ in range(position - 1):
            current = current.next
            
        current.next = current.next.next
        self.size -= 1

    def search(self, data):
        """
        Search for a node with the given data.
        
        Args:
            data: The data to search for
            
        Returns:
            The position of the node if found, -1 otherwise
        """
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
            
        return -1

    def get_size(self):
        """
        Return the number of nodes in the linked list.
        
        Returns:
            The number of nodes in the linked list
        """
        return self.size

    def clear(self):
        """Remove all nodes from the linked list."""
        self.head = None
        self.size = 0

    def __str__(self):
        """
        Return a string representation of the linked list.
        
        Returns:
            A string representation of the linked list
        """
        if self.is_empty():
            return "Empty linked list"
            
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
            
        return " -> ".join(result)


# Example usage
if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()
    
    # Insert some nodes
    ll.insert_at_beginning(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_position(4, 1)
    
    print(f"Linked list: {ll}")  # Output: Linked list: 1 -> 4 -> 2 -> 3
    print(f"Size: {ll.get_size()}")  # Output: Size: 4
    
    # Search for a node
    position = ll.search(4)
    print(f"Position of 4: {position}")  # Output: Position of 4: 1
    
    # Delete nodes
    ll.delete_at_position(1)
    print(f"After deletion: {ll}")  # Output: After deletion: 1 -> 2 -> 3
    
    # Clear the linked list
    ll.clear()
    print(f"After clearing: {ll}")  # Output: After clearing: Empty linked list 
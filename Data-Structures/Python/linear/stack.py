"""
Stack Implementation in Python

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
Elements are added and removed from the same end, called the top of the stack.

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)

Space Complexity: O(n)
"""

class Stack:
    """
    A simple implementation of a Stack data structure.
    
    A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
    Elements are added and removed from the same end (top) of the stack.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """
        Return the top item from the stack without removing it.
        
        Returns:
            The top item from the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of items in the stack.
        
        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)
    
    def __str__(self):
        """
        Return a string representation of the stack.
        
        Returns:
            str: A string representation of the stack.
        """
        return str(self.items)


# Example usage
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()
    
    # Push some items
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    print(f"Top item: {stack.peek()}")
    
    # Pop items
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack after popping: {stack}") 
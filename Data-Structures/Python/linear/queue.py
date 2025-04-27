"""
Queue Implementation in Python

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
Elements are added at the rear and removed from the front of the queue.

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)
- Search: O(n)

Space Complexity: O(n)
"""

from collections import deque

class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = deque()

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to be added to the queue
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def peek(self):
        """
        Return the front item from the queue without removing it.
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of items in the queue.
        
        Returns:
            The number of items in the queue
        """
        return len(self.items)

    def clear(self):
        """Remove all items from the queue."""
        self.items.clear()


# Example usage
if __name__ == "__main__":
    # Create a new queue
    queue = Queue()
    
    # Enqueue some items
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print(f"Queue size: {queue.size()}")  # Output: Queue size: 3
    print(f"Front item: {queue.peek()}")  # Output: Front item: 1
    
    # Dequeue items
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}")
    
    # Output:
    # Dequeued: 1
    # Dequeued: 2
    # Dequeued: 3 
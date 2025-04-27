from typing import Optional, List, Any

class CircularQueue:
    """
    A Circular Queue implementation.
    
    A Circular Queue is a linear data structure that follows the First-In-First-Out (FIFO)
    principle, but with a fixed size and circular behavior. When the queue is full,
    new elements can be added by overwriting the oldest elements.
    """
    
    def __init__(self, capacity: int):
        """
        Initialize a Circular Queue.
        
        Args:
            capacity: The maximum number of elements the queue can hold.
        """
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, item: Any) -> None:
        """
        Add an item to the queue.
        If the queue is full, the oldest item will be overwritten.
        
        Args:
            item: The item to be added to the queue.
        """
        if self.is_full():
            # If queue is full, move front pointer to overwrite oldest item
            self.front = (self.front + 1) % self.capacity
        else:
            self.size += 1
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
    
    def dequeue(self) -> Optional[Any]:
        """
        Remove and return the front item from the queue.
        
        Returns:
            The front item from the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        
        return item
    
    def peek(self) -> Optional[Any]:
        """
        Return the front item from the queue without removing it.
        
        Returns:
            The front item from the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.queue[self.front]
    
    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.size == 0
    
    def is_full(self) -> bool:
        """
        Check if the queue is full.
        
        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self.size == self.capacity
    
    def get_size(self) -> int:
        """
        Get the number of items in the queue.
        
        Returns:
            int: The number of items in the queue.
        """
        return self.size
    
    def clear(self) -> None:
        """Remove all items from the queue."""
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def to_list(self) -> List[Any]:
        """
        Convert the queue to a list.
        
        Returns:
            List[Any]: A list containing all items in the queue.
        """
        if self.is_empty():
            return []
        
        result = []
        current = self.front
        for _ in range(self.size):
            result.append(self.queue[current])
            current = (current + 1) % self.capacity
        
        return result
    
    def __str__(self) -> str:
        """
        Return a string representation of the queue.
        
        Returns:
            str: A string representation of the queue.
        """
        return str(self.to_list())


# Example usage
if __name__ == "__main__":
    # Create a circular queue with capacity 5
    queue = CircularQueue(5)
    
    # Enqueue some items
    for i in range(1, 8):
        queue.enqueue(i)
        print(f"After enqueueing {i}: {queue}")
    
    # Dequeue some items
    for _ in range(3):
        item = queue.dequeue()
        print(f"Dequeued: {item}")
        print(f"Queue after dequeue: {queue}")
    
    # Enqueue more items
    for i in range(8, 11):
        queue.enqueue(i)
        print(f"After enqueueing {i}: {queue}")
    
    # Peek at the front item
    print(f"Front item: {queue.peek()}")
    
    # Get queue size
    print(f"Queue size: {queue.get_size()}")
    
    # Clear the queue
    queue.clear()
    print(f"Queue after clearing: {queue}") 
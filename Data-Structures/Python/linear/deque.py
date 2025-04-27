from typing import Optional, List, Any

class Deque:
    """
    A Deque (double-ended queue) implementation.
    
    A Deque is a linear data structure that allows insertion and deletion
    of elements from both ends. It combines the features of a stack and a queue.
    """
    
    def __init__(self):
        """Initialize an empty Deque."""
        self.items = []
    
    def add_front(self, item: Any) -> None:
        """
        Add an item to the front of the deque.
        
        Args:
            item: The item to be added to the front.
        """
        self.items.insert(0, item)
    
    def add_rear(self, item: Any) -> None:
        """
        Add an item to the rear of the deque.
        
        Args:
            item: The item to be added to the rear.
        """
        self.items.append(item)
    
    def remove_front(self) -> Optional[Any]:
        """
        Remove and return the front item from the deque.
        
        Returns:
            The front item from the deque, or None if the deque is empty.
        """
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def remove_rear(self) -> Optional[Any]:
        """
        Remove and return the rear item from the deque.
        
        Returns:
            The rear item from the deque, or None if the deque is empty.
        """
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek_front(self) -> Optional[Any]:
        """
        Return the front item from the deque without removing it.
        
        Returns:
            The front item from the deque, or None if the deque is empty.
        """
        if self.is_empty():
            return None
        return self.items[0]
    
    def peek_rear(self) -> Optional[Any]:
        """
        Return the rear item from the deque without removing it.
        
        Returns:
            The rear item from the deque, or None if the deque is empty.
        """
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self) -> bool:
        """
        Check if the deque is empty.
        
        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in the deque.
        
        Returns:
            int: The number of items in the deque.
        """
        return len(self.items)
    
    def clear(self) -> None:
        """Remove all items from the deque."""
        self.items.clear()
    
    def to_list(self) -> List[Any]:
        """
        Convert the deque to a list.
        
        Returns:
            List[Any]: A list containing all items in the deque.
        """
        return self.items.copy()
    
    def __str__(self) -> str:
        """
        Return a string representation of the deque.
        
        Returns:
            str: A string representation of the deque.
        """
        return str(self.items)


# Example usage
if __name__ == "__main__":
    deque = Deque()
    
    # Add items to front and rear
    deque.add_front(1)
    deque.add_rear(2)
    deque.add_front(3)
    deque.add_rear(4)
    
    print(f"Deque: {deque}")
    print(f"Size: {deque.size()}")
    
    # Peek at front and rear
    print(f"Front item: {deque.peek_front()}")
    print(f"Rear item: {deque.peek_rear()}")
    
    # Remove items from front and rear
    print(f"Removed from front: {deque.remove_front()}")
    print(f"Removed from rear: {deque.remove_rear()}")
    
    print(f"Deque after removals: {deque}")
    
    # Clear the deque
    deque.clear()
    print(f"Deque after clearing: {deque}") 
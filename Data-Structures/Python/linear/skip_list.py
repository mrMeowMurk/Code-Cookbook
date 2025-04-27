import random
from typing import Optional, List, Tuple

class SkipListNode:
    """
    A node in the Skip List data structure.
    Each node contains a value and a list of forward pointers.
    """
    def __init__(self, value: float, level: int):
        self.value = value
        self.forward = [None] * level

class SkipList:
    """
    A Skip List implementation.
    
    A Skip List is a probabilistic data structure that allows for efficient
    search, insertion, and deletion operations with O(log n) average time complexity.
    """
    
    def __init__(self, max_level: int = 16, p: float = 0.5):
        """
        Initialize a Skip List.
        
        Args:
            max_level: Maximum number of levels in the skip list.
            p: Probability of a node being promoted to the next level.
        """
        self.max_level = max_level
        self.p = p
        self.level = 0
        self.header = SkipListNode(float('-inf'), max_level)
        self.size = 0
    
    def _random_level(self) -> int:
        """
        Generate a random level for a new node.
        
        Returns:
            int: A random level between 1 and max_level.
        """
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def search(self, value: float) -> bool:
        """
        Search for a value in the Skip List.
        
        Args:
            value: The value to search for.
            
        Returns:
            bool: True if the value exists in the Skip List, False otherwise.
        """
        current = self.header
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        
        current = current.forward[0]
        return current is not None and current.value == value
    
    def insert(self, value: float) -> None:
        """
        Insert a value into the Skip List.
        
        Args:
            value: The value to insert.
        """
        update = [None] * self.max_level
        current = self.header
        
        # Find the position to insert
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # If value already exists, don't insert
        if current is not None and current.value == value:
            return
        
        # Generate random level for new node
        new_level = self._random_level()
        
        # Update max level if necessary
        if new_level > self.level:
            for i in range(self.level, new_level):
                update[i] = self.header
            self.level = new_level
        
        # Create new node
        new_node = SkipListNode(value, new_level)
        
        # Update forward pointers
        for i in range(new_level):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
        
        self.size += 1
    
    def delete(self, value: float) -> bool:
        """
        Delete a value from the Skip List.
        
        Args:
            value: The value to delete.
            
        Returns:
            bool: True if the value was deleted, False if it didn't exist.
        """
        update = [None] * self.max_level
        current = self.header
        
        # Find the position to delete
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # If value doesn't exist, return False
        if current is None or current.value != value:
            return False
        
        # Update forward pointers
        for i in range(self.level):
            if update[i].forward[i] != current:
                break
            update[i].forward[i] = current.forward[i]
        
        # Update max level if necessary
        while self.level > 0 and self.header.forward[self.level - 1] is None:
            self.level -= 1
        
        self.size -= 1
        return True
    
    def get_range(self, start: float, end: float) -> List[float]:
        """
        Get all values in the Skip List within a given range.
        
        Args:
            start: The start of the range (inclusive).
            end: The end of the range (inclusive).
            
        Returns:
            List[float]: A list of values within the range.
        """
        result = []
        current = self.header
        
        # Find the first node in the range
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < start:
                current = current.forward[i]
        
        current = current.forward[0]
        
        # Collect all values in the range
        while current and current.value <= end:
            result.append(current.value)
            current = current.forward[0]
        
        return result
    
    def __str__(self) -> str:
        """
        Return a string representation of the Skip List.
        
        Returns:
            str: A string representation of the Skip List.
        """
        result = []
        for i in range(self.level - 1, -1, -1):
            level_str = f"Level {i}: "
            current = self.header
            while current:
                level_str += f"{current.value} -> "
                current = current.forward[i]
            level_str += "None"
            result.append(level_str)
        return "\n".join(result)


# Example usage
if __name__ == "__main__":
    skip_list = SkipList()
    
    # Insert some values
    values = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
    for value in values:
        skip_list.insert(value)
    
    print("Skip List after insertion:")
    print(skip_list)
    
    # Search for values
    print(f"\nSearch 7: {skip_list.search(7)}")  # True
    print(f"Search 8: {skip_list.search(8)}")    # False
    
    # Get values in range
    print(f"\nValues in range [7, 20]: {skip_list.get_range(7, 20)}")
    
    # Delete a value
    print(f"\nDelete 7: {skip_list.delete(7)}")  # True
    print(f"Search 7 after deletion: {skip_list.search(7)}")  # False
    
    print("\nSkip List after deletion:")
    print(skip_list) 
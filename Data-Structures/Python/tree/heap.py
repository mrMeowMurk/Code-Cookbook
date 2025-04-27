"""
Heap Implementation in Python

A heap is a specialized tree-based data structure that satisfies the heap property:
- In a max heap, for any given node N, the value of N is greater than or equal to the values of its children.
- In a min heap, for any given node N, the value of N is less than or equal to the values of its children.

Time Complexity:
- Insert: O(log n)
- Delete: O(log n)
- Get max/min: O(1)
- Heapify: O(n)

Space Complexity: O(n)
"""

class Heap:
    def __init__(self, max_heap=True):
        """
        Initialize a new heap.
        
        Args:
            max_heap: Whether this is a max heap (True) or min heap (False)
        """
        self.heap = []
        self.max_heap = max_heap

    def _parent(self, i):
        """
        Get the index of the parent of a node.
        
        Args:
            i: The index of the node
            
        Returns:
            The index of the parent
        """
        return (i - 1) // 2

    def _left_child(self, i):
        """
        Get the index of the left child of a node.
        
        Args:
            i: The index of the node
            
        Returns:
            The index of the left child
        """
        return 2 * i + 1

    def _right_child(self, i):
        """
        Get the index of the right child of a node.
        
        Args:
            i: The index of the node
            
        Returns:
            The index of the right child
        """
        return 2 * i + 2

    def _swap(self, i, j):
        """
        Swap two elements in the heap.
        
        Args:
            i: The index of the first element
            j: The index of the second element
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _compare(self, i, j):
        """
        Compare two elements in the heap.
        
        Args:
            i: The index of the first element
            j: The index of the second element
            
        Returns:
            True if the first element should be above the second element in the heap
        """
        if self.max_heap:
            return self.heap[i] > self.heap[j]
        else:
            return self.heap[i] < self.heap[j]

    def _heapify_up(self, i):
        """
        Restore the heap property by moving an element up.
        
        Args:
            i: The index of the element to move up
        """
        parent = self._parent(i)
        if i > 0 and self._compare(i, parent):
            self._swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i):
        """
        Restore the heap property by moving an element down.
        
        Args:
            i: The index of the element to move down
        """
        left = self._left_child(i)
        right = self._right_child(i)
        largest = i

        if left < len(self.heap) and self._compare(left, largest):
            largest = left

        if right < len(self.heap) and self._compare(right, largest):
            largest = right

        if largest != i:
            self._swap(i, largest)
            self._heapify_down(largest)

    def insert(self, value):
        """
        Insert a value into the heap.
        
        Args:
            value: The value to insert
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        """
        Delete the root element from the heap.
        
        Returns:
            The root element
            
        Raises:
            IndexError: If the heap is empty
        """
        if not self.heap:
            raise IndexError("Heap is empty")

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)

        return root

    def peek(self):
        """
        Get the root element without removing it.
        
        Returns:
            The root element
            
        Raises:
            IndexError: If the heap is empty
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self):
        """
        Get the number of elements in the heap.
        
        Returns:
            The number of elements
        """
        return len(self.heap)

    def is_empty(self):
        """
        Check if the heap is empty.
        
        Returns:
            True if the heap is empty, False otherwise
        """
        return len(self.heap) == 0

    def clear(self):
        """Remove all elements from the heap."""
        self.heap.clear()

    def heapify(self, values):
        """
        Build a heap from a list of values.
        
        Args:
            values: The list of values to build the heap from
        """
        self.heap = values
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)


# Example usage
if __name__ == "__main__":
    # Create a max heap
    max_heap = Heap(max_heap=True)
    
    # Insert some values
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(30)
    max_heap.insert(40)
    max_heap.insert(50)
    
    print(f"Size: {max_heap.size()}")  # Output: Size: 5
    print(f"Is empty: {max_heap.is_empty()}")  # Output: Is empty: False
    print(f"Peek: {max_heap.peek()}")  # Output: Peek: 50
    
    # Delete elements
    print(f"Deleted: {max_heap.delete()}")  # Output: Deleted: 50
    print(f"Deleted: {max_heap.delete()}")  # Output: Deleted: 40
    print(f"Peek after deletions: {max_heap.peek()}")  # Output: Peek after deletions: 30
    
    # Create a min heap
    min_heap = Heap(max_heap=False)
    
    # Insert some values
    min_heap.insert(10)
    min_heap.insert(20)
    min_heap.insert(30)
    min_heap.insert(40)
    min_heap.insert(50)
    
    print(f"Peek: {min_heap.peek()}")  # Output: Peek: 10
    
    # Delete elements
    print(f"Deleted: {min_heap.delete()}")  # Output: Deleted: 10
    print(f"Deleted: {min_heap.delete()}")  # Output: Deleted: 20
    print(f"Peek after deletions: {min_heap.peek()}")  # Output: Peek after deletions: 30
    
    # Build a heap from a list
    values = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    heap = Heap(max_heap=True)
    heap.heapify(values)
    
    print(f"Peek after heapify: {heap.peek()}")  # Output: Peek after heapify: 9
    
    # Clear the heap
    heap.clear()
    print(f"Size after clearing: {heap.size()}")  # Output: Size after clearing: 0
    print(f"Is empty after clearing: {heap.is_empty()}")  # Output: Is empty after clearing: True 
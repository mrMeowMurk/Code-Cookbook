"""
Hash Table Implementation in Python

A hash table is a data structure that implements an associative array abstract data type,
a structure that can map keys to values. It uses a hash function to compute an index into
an array of buckets or slots, from which the desired value can be found.

Time Complexity:
- Insert: O(1) average case, O(n) worst case
- Delete: O(1) average case, O(n) worst case
- Search: O(1) average case, O(n) worst case

Space Complexity: O(n)
"""

class HashTable:
    def __init__(self, initial_size=10, load_factor=0.75):
        """
        Initialize a new hash table.
        
        Args:
            initial_size: The initial size of the hash table
            load_factor: The load factor threshold for resizing
        """
        self.size = initial_size
        self.load_factor = load_factor
        self.count = 0
        self.table = [[] for _ in range(initial_size)]

    def _hash(self, key):
        """
        Compute the hash value for a key.
        
        Args:
            key: The key to hash
            
        Returns:
            The hash value
        """
        return hash(key) % self.size

    def _resize(self):
        """Resize the hash table when the load factor is exceeded."""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        
        Args:
            key: The key to insert
            value: The value to insert
        """
        if self.count / self.size >= self.load_factor:
            self._resize()

        index = self._hash(key)
        bucket = self.table[index]

        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        
        Args:
            key: The key to delete
            
        Returns:
            True if the key was deleted, False otherwise
        """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return True

        return False

    def search(self, key):
        """
        Search for a value by key in the hash table.
        
        Args:
            key: The key to search for
            
        Returns:
            The value associated with the key, or None if not found
        """
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def get_size(self):
        """
        Get the number of key-value pairs in the hash table.
        
        Returns:
            The number of key-value pairs
        """
        return self.count

    def is_empty(self):
        """
        Check if the hash table is empty.
        
        Returns:
            True if the hash table is empty, False otherwise
        """
        return self.count == 0

    def clear(self):
        """Remove all key-value pairs from the hash table."""
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def keys(self):
        """
        Get all keys in the hash table.
        
        Returns:
            A list of all keys
        """
        keys = []
        for bucket in self.table:
            for key, _ in bucket:
                keys.append(key)
        return keys

    def values(self):
        """
        Get all values in the hash table.
        
        Returns:
            A list of all values
        """
        values = []
        for bucket in self.table:
            for _, value in bucket:
                values.append(value)
        return values

    def items(self):
        """
        Get all key-value pairs in the hash table.
        
        Returns:
            A list of (key, value) tuples
        """
        items = []
        for bucket in self.table:
            items.extend(bucket)
        return items


# Example usage
if __name__ == "__main__":
    # Create a new hash table
    ht = HashTable()
    
    # Insert some key-value pairs
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("cherry", 3)
    ht.insert("date", 4)
    ht.insert("elderberry", 5)
    
    print(f"Size: {ht.get_size()}")  # Output: Size: 5
    print(f"Is empty: {ht.is_empty()}")  # Output: Is empty: False
    
    # Search for values
    print(f"Value for 'banana': {ht.search('banana')}")  # Output: Value for 'banana': 2
    print(f"Value for 'fig': {ht.search('fig')}")  # Output: Value for 'fig': None
    
    # Update a value
    ht.insert("banana", 20)
    print(f"Updated value for 'banana': {ht.search('banana')}")  # Output: Updated value for 'banana': 20
    
    # Delete a key-value pair
    ht.delete("cherry")
    print(f"Value for 'cherry' after deletion: {ht.search('cherry')}")  # Output: Value for 'cherry' after deletion: None
    
    # Get all keys, values, and items
    print(f"Keys: {ht.keys()}")  # Output: Keys: ['apple', 'banana', 'date', 'elderberry']
    print(f"Values: {ht.values()}")  # Output: Values: [1, 20, 4, 5]
    print(f"Items: {ht.items()}")  # Output: Items: [('apple', 1), ('banana', 20), ('date', 4), ('elderberry', 5)]
    
    # Clear the hash table
    ht.clear()
    print(f"Size after clearing: {ht.get_size()}")  # Output: Size after clearing: 0
    print(f"Is empty after clearing: {ht.is_empty()}")  # Output: Is empty after clearing: True 
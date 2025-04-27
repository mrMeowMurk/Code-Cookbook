class HashTable:
    def __init__(self, size):
        """
        Initialize hash table with given size
        """
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash_function(self, key):
        """
        Simple hash function
        """
        return key % self.size
    
    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table
        """
        hash_value = self._hash_function(key)
        self.table[hash_value].append((key, value))
    
    def search(self, key):
        """
        Search for a key in the hash table
        Time Complexity: O(1) average case, O(n) worst case
        Space Complexity: O(n)
        """
        hash_value = self._hash_function(key)
        
        # Search in the chain
        for item in self.table[hash_value]:
            if item[0] == key:
                return item[1]  # Return the value
        
        return None  # Key not found

# Example usage
if __name__ == "__main__":
    # Create a hash table
    hash_table = HashTable(10)
    
    # Insert some key-value pairs
    hash_table.insert(1, "One")
    hash_table.insert(2, "Two")
    hash_table.insert(11, "Eleven")  # This will cause a collision with key 1
    
    # Search for keys
    print("Searching for key 1:", hash_table.search(1))
    print("Searching for key 2:", hash_table.search(2))
    print("Searching for key 11:", hash_table.search(11))
    print("Searching for key 3:", hash_table.search(3))  # Not found 
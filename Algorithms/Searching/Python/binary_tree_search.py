class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """
        Insert a new key into the BST
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        """
        Helper function for recursive insertion
        """
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
    
    def search(self, key):
        """
        Search for a key in the BST
        Time Complexity: O(h) where h is the height of the tree
        Space Complexity: O(1)
        """
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        """
        Helper function for recursive search
        """
        # Base cases: root is null or key is present at root
        if node is None or node.val == key:
            return node
        
        # Key is greater than root's key
        if key > node.val:
            return self._search_recursive(node.right, key)
        
        # Key is smaller than root's key
        return self._search_recursive(node.left, key)

# Example usage
if __name__ == "__main__":
    # Create a BST
    bst = BinarySearchTree()
    
    # Insert some keys
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)
    
    # Search for keys
    search_keys = [40, 90, 20]
    for key in search_keys:
        result = bst.search(key)
        if result:
            print(f"Key {key} found in the BST")
        else:
            print(f"Key {key} not found in the BST") 
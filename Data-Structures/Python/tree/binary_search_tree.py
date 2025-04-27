"""
Binary Search Tree Implementation in Python

A binary search tree is a binary tree where each node has a value greater than all values
in its left subtree and less than all values in its right subtree.

Time Complexity:
- Insert: O(log n) average case, O(n) worst case
- Delete: O(log n) average case, O(n) worst case
- Search: O(log n) average case, O(n) worst case
- Traversal: O(n)

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
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root = None

    def is_empty(self):
        """
        Check if the binary search tree is empty.
        
        Returns:
            True if the binary search tree is empty, False otherwise
        """
        return self.root is None

    def insert(self, data):
        """
        Insert a new node into the binary search tree.
        
        Args:
            data: The data to be inserted
        """
        if self.is_empty():
            self.root = Node(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right

    def delete(self, data):
        """
        Delete a node with the given data from the binary search tree.
        
        Args:
            data: The data to be deleted
            
        Returns:
            True if the node was deleted, False otherwise
        """
        if self.is_empty():
            return False

        # Find the node to be deleted and its parent
        current = self.root
        parent = None
        is_left_child = False

        while current and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
                is_left_child = True
            else:
                current = current.right
                is_left_child = False

        if current is None:
            return False

        # Case 1: Node to be deleted is a leaf node
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif is_left_child:
                parent.left = None
            else:
                parent.right = None
            return True

        # Case 2: Node to be deleted has only one child
        if current.left is None:
            if parent is None:
                self.root = current.right
            elif is_left_child:
                parent.left = current.right
            else:
                parent.right = current.right
            return True

        if current.right is None:
            if parent is None:
                self.root = current.left
            elif is_left_child:
                parent.left = current.left
            else:
                parent.right = current.left
            return True

        # Case 3: Node to be deleted has two children
        # Find the inorder successor (smallest node in the right subtree)
        successor = current.right
        successor_parent = current
        is_successor_left_child = False

        while successor.left:
            successor_parent = successor
            successor = successor.left
            is_successor_left_child = True

        # Replace the node to be deleted with its successor
        current.data = successor.data

        # Delete the successor
        if is_successor_left_child:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

        return True

    def search(self, data):
        """
        Search for a node with the given data in the binary search tree.
        
        Args:
            data: The data to search for
            
        Returns:
            True if the node is found, False otherwise
        """
        if self.is_empty():
            return False

        current = self.root
        while current:
            if data == current.data:
                return True
            if data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the binary search tree.
        
        Returns:
            A list containing the nodes in inorder traversal order
        """
        result = []
        
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.data)
                inorder(node.right)
                
        inorder(self.root)
        return result

    def preorder_traversal(self):
        """
        Perform a preorder traversal of the binary search tree.
        
        Returns:
            A list containing the nodes in preorder traversal order
        """
        result = []
        
        def preorder(node):
            if node:
                result.append(node.data)
                preorder(node.left)
                preorder(node.right)
                
        preorder(self.root)
        return result

    def postorder_traversal(self):
        """
        Perform a postorder traversal of the binary search tree.
        
        Returns:
            A list containing the nodes in postorder traversal order
        """
        result = []
        
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                result.append(node.data)
                
        postorder(self.root)
        return result

    def get_min(self):
        """
        Get the minimum value in the binary search tree.
        
        Returns:
            The minimum value in the binary search tree
            
        Raises:
            ValueError: If the binary search tree is empty
        """
        if self.is_empty():
            raise ValueError("Binary search tree is empty")

        current = self.root
        while current.left:
            current = current.left

        return current.data

    def get_max(self):
        """
        Get the maximum value in the binary search tree.
        
        Returns:
            The maximum value in the binary search tree
            
        Raises:
            ValueError: If the binary search tree is empty
        """
        if self.is_empty():
            raise ValueError("Binary search tree is empty")

        current = self.root
        while current.right:
            current = current.right

        return current.data

    def get_height(self):
        """
        Get the height of the binary search tree.
        
        Returns:
            The height of the binary search tree
        """
        def height(node):
            if node is None:
                return 0
            return max(height(node.left), height(node.right)) + 1
            
        return height(self.root)

    def clear(self):
        """Remove all nodes from the binary search tree."""
        self.root = None


# Example usage
if __name__ == "__main__":
    # Create a new binary search tree
    bst = BinarySearchTree()
    
    # Insert some nodes
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(9)
    
    print(f"Inorder traversal: {bst.inorder_traversal()}")  # Output: [1, 3, 5, 7, 9]
    print(f"Preorder traversal: {bst.preorder_traversal()}")  # Output: [5, 3, 1, 7, 9]
    print(f"Postorder traversal: {bst.postorder_traversal()}")  # Output: [1, 3, 9, 7, 5]
    
    print(f"Minimum value: {bst.get_min()}")  # Output: Minimum value: 1
    print(f"Maximum value: {bst.get_max()}")  # Output: Maximum value: 9
    print(f"Height: {bst.get_height()}")  # Output: Height: 3
    
    # Search for a node
    print(f"Search for 3: {bst.search(3)}")  # Output: Search for 3: True
    print(f"Search for 6: {bst.search(6)}")  # Output: Search for 6: False
    
    # Delete a node
    bst.delete(3)
    print(f"After deleting 3: {bst.inorder_traversal()}")  # Output: After deleting 3: [1, 5, 7, 9]
    
    # Clear the tree
    bst.clear()
    print(f"After clearing: {bst.inorder_traversal()}")  # Output: After clearing: [] 
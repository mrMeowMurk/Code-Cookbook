"""
AVL Tree Implementation in Python

An AVL tree is a self-balancing binary search tree where the heights of the left and right
subtrees of any node differ by at most one.

Time Complexity:
- Insert: O(log n)
- Delete: O(log n)
- Search: O(log n)
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
        self.height = 1

class AVLTree:
    def __init__(self):
        """Initialize an empty AVL tree."""
        self.root = None

    def is_empty(self):
        """
        Check if the AVL tree is empty.
        
        Returns:
            True if the AVL tree is empty, False otherwise
        """
        return self.root is None

    def get_height(self, node):
        """
        Get the height of a node.
        
        Args:
            node: The node to get the height of
            
        Returns:
            The height of the node, 0 if the node is None
        """
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        """
        Get the balance factor of a node.
        
        Args:
            node: The node to get the balance factor of
            
        Returns:
            The balance factor of the node
        """
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        """
        Perform a right rotation.
        
        Args:
            y: The node to rotate around
            
        Returns:
            The new root of the subtree
        """
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        """
        Perform a left rotation.
        
        Args:
            x: The node to rotate around
            
        Returns:
            The new root of the subtree
        """
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, data):
        """
        Insert a new node into the AVL tree.
        
        Args:
            data: The data to be inserted
        """
        def insert_recursive(node, data):
            if node is None:
                return Node(data)

            if data < node.data:
                node.left = insert_recursive(node.left, data)
            else:
                node.right = insert_recursive(node.right, data)

            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

            balance = self.get_balance(node)

            # Left Left Case
            if balance > 1 and data < node.left.data:
                return self.right_rotate(node)

            # Right Right Case
            if balance < -1 and data > node.right.data:
                return self.left_rotate(node)

            # Left Right Case
            if balance > 1 and data > node.left.data:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

            # Right Left Case
            if balance < -1 and data < node.right.data:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

            return node

        self.root = insert_recursive(self.root, data)

    def delete(self, data):
        """
        Delete a node with the given data from the AVL tree.
        
        Args:
            data: The data to be deleted
            
        Returns:
            True if the node was deleted, False otherwise
        """
        def delete_recursive(node, data):
            if node is None:
                return None

            if data < node.data:
                node.left = delete_recursive(node.left, data)
            elif data > node.data:
                node.right = delete_recursive(node.right, data)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Node with two children: Get the inorder successor
                temp = node.right
                while temp.left:
                    temp = temp.left

                node.data = temp.data
                node.right = delete_recursive(node.right, temp.data)

            if node is None:
                return None

            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

            balance = self.get_balance(node)

            # Left Left Case
            if balance > 1 and self.get_balance(node.left) >= 0:
                return self.right_rotate(node)

            # Left Right Case
            if balance > 1 and self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

            # Right Right Case
            if balance < -1 and self.get_balance(node.right) <= 0:
                return self.left_rotate(node)

            # Right Left Case
            if balance < -1 and self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

            return node

        if self.is_empty():
            return False

        self.root = delete_recursive(self.root, data)
        return True

    def search(self, data):
        """
        Search for a node with the given data in the AVL tree.
        
        Args:
            data: The data to search for
            
        Returns:
            True if the node is found, False otherwise
        """
        def search_recursive(node, data):
            if node is None:
                return False

            if data == node.data:
                return True
            elif data < node.data:
                return search_recursive(node.left, data)
            else:
                return search_recursive(node.right, data)

        return search_recursive(self.root, data)

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the AVL tree.
        
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
        Perform a preorder traversal of the AVL tree.
        
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
        Perform a postorder traversal of the AVL tree.
        
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
        Get the minimum value in the AVL tree.
        
        Returns:
            The minimum value in the AVL tree
            
        Raises:
            ValueError: If the AVL tree is empty
        """
        if self.is_empty():
            raise ValueError("AVL tree is empty")

        current = self.root
        while current.left:
            current = current.left

        return current.data

    def get_max(self):
        """
        Get the maximum value in the AVL tree.
        
        Returns:
            The maximum value in the AVL tree
            
        Raises:
            ValueError: If the AVL tree is empty
        """
        if self.is_empty():
            raise ValueError("AVL tree is empty")

        current = self.root
        while current.right:
            current = current.right

        return current.data

    def clear(self):
        """Remove all nodes from the AVL tree."""
        self.root = None


# Example usage
if __name__ == "__main__":
    # Create a new AVL tree
    avl = AVLTree()
    
    # Insert some nodes
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)
    avl.insert(25)
    
    print(f"Inorder traversal: {avl.inorder_traversal()}")  # Output: [10, 20, 25, 30, 40, 50]
    print(f"Preorder traversal: {avl.preorder_traversal()}")  # Output: [30, 20, 10, 25, 40, 50]
    print(f"Postorder traversal: {avl.postorder_traversal()}")  # Output: [10, 25, 20, 50, 40, 30]
    
    print(f"Minimum value: {avl.get_min()}")  # Output: Minimum value: 10
    print(f"Maximum value: {avl.get_max()}")  # Output: Maximum value: 50
    
    # Search for a node
    print(f"Search for 25: {avl.search(25)}")  # Output: Search for 25: True
    print(f"Search for 35: {avl.search(35)}")  # Output: Search for 35: False
    
    # Delete a node
    avl.delete(30)
    print(f"After deleting 30: {avl.inorder_traversal()}")  # Output: After deleting 30: [10, 20, 25, 40, 50]
    
    # Clear the tree
    avl.clear()
    print(f"After clearing: {avl.inorder_traversal()}")  # Output: After clearing: [] 
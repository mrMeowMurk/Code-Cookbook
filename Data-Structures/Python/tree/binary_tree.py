"""
Binary Tree Implementation in Python

A binary tree is a tree data structure in which each node has at most two children,
referred to as the left child and the right child.

Time Complexity:
- Insert: O(n) in worst case
- Delete: O(n) in worst case
- Search: O(n) in worst case
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

class BinaryTree:
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None

    def is_empty(self):
        """
        Check if the binary tree is empty.
        
        Returns:
            True if the binary tree is empty, False otherwise
        """
        return self.root is None

    def insert(self, data):
        """
        Insert a new node into the binary tree.
        
        Args:
            data: The data to be inserted
        """
        if self.is_empty():
            self.root = Node(data)
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            if node.left is None:
                node.left = Node(data)
                return
            queue.append(node.left)
            
            if node.right is None:
                node.right = Node(data)
                return
            queue.append(node.right)

    def delete(self, data):
        """
        Delete a node with the given data from the binary tree.
        
        Args:
            data: The data to be deleted
            
        Returns:
            True if the node was deleted, False otherwise
        """
        if self.is_empty():
            return False

        # Find the node to be deleted and its parent
        node_to_delete = None
        parent = None
        queue = [(self.root, None)]
        
        while queue:
            node, parent_node = queue.pop(0)
            
            if node.data == data:
                node_to_delete = node
                parent = parent_node
                break
                
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))

        if node_to_delete is None:
            return False

        # If the node to be deleted is a leaf node
        if node_to_delete.left is None and node_to_delete.right is None:
            if parent is None:
                self.root = None
            elif parent.left == node_to_delete:
                parent.left = None
            else:
                parent.right = None
            return True

        # If the node to be deleted has only one child
        if node_to_delete.left is None:
            if parent is None:
                self.root = node_to_delete.right
            elif parent.left == node_to_delete:
                parent.left = node_to_delete.right
            else:
                parent.right = node_to_delete.right
            return True
            
        if node_to_delete.right is None:
            if parent is None:
                self.root = node_to_delete.left
            elif parent.left == node_to_delete:
                parent.left = node_to_delete.left
            else:
                parent.right = node_to_delete.left
            return True

        # If the node to be deleted has two children
        # Find the inorder successor (smallest node in the right subtree)
        successor = node_to_delete.right
        successor_parent = node_to_delete
        
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # Replace the node to be deleted with its successor
        node_to_delete.data = successor.data
        
        # Delete the successor
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right
            
        return True

    def search(self, data):
        """
        Search for a node with the given data in the binary tree.
        
        Args:
            data: The data to search for
            
        Returns:
            True if the node is found, False otherwise
        """
        if self.is_empty():
            return False

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            if node.data == data:
                return True
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return False

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the binary tree.
        
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
        Perform a preorder traversal of the binary tree.
        
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
        Perform a postorder traversal of the binary tree.
        
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

    def level_order_traversal(self):
        """
        Perform a level order traversal of the binary tree.
        
        Returns:
            A list containing the nodes in level order traversal order
        """
        if self.is_empty():
            return []
            
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result

    def get_height(self):
        """
        Get the height of the binary tree.
        
        Returns:
            The height of the binary tree
        """
        def height(node):
            if node is None:
                return 0
            return max(height(node.left), height(node.right)) + 1
            
        return height(self.root)

    def clear(self):
        """Remove all nodes from the binary tree."""
        self.root = None


# Example usage
if __name__ == "__main__":
    # Create a new binary tree
    tree = BinaryTree()
    
    # Insert some nodes
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    
    print(f"Inorder traversal: {tree.inorder_traversal()}")  # Output: [4, 2, 5, 1, 3]
    print(f"Preorder traversal: {tree.preorder_traversal()}")  # Output: [1, 2, 4, 5, 3]
    print(f"Postorder traversal: {tree.postorder_traversal()}")  # Output: [4, 5, 2, 3, 1]
    print(f"Level order traversal: {tree.level_order_traversal()}")  # Output: [1, 2, 3, 4, 5]
    print(f"Height: {tree.get_height()}")  # Output: Height: 3
    
    # Search for a node
    print(f"Search for 4: {tree.search(4)}")  # Output: Search for 4: True
    print(f"Search for 6: {tree.search(6)}")  # Output: Search for 6: False
    
    # Delete a node
    tree.delete(2)
    print(f"After deleting 2: {tree.level_order_traversal()}")  # Output: After deleting 2: [1, 3, 4, 5]
    
    # Clear the tree
    tree.clear()
    print(f"After clearing: {tree.level_order_traversal()}")  # Output: After clearing: [] 
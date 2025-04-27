class TrieNode:
    """
    A node in the Trie data structure.
    Each node represents a character in a word.
    """
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to mark end of word
        self.word_count = 0  # Count of words ending at this node

class Trie:
    """
    A Trie (prefix tree) implementation.
    
    A Trie is a tree-like data structure used to store and retrieve strings.
    It is particularly efficient for operations like:
    - Inserting a string
    - Searching for a string
    - Finding all strings with a given prefix
    """
    
    def __init__(self):
        """Initialize an empty Trie."""
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.
        
        Args:
            word: The word to be inserted.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word_count += 1
    
    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.
        
        Args:
            word: The word to search for.
            
        Returns:
            bool: True if the word exists in the Trie, False otherwise.
        """
        node = self._get_node(word)
        return node is not None and node.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the Trie starts with the given prefix.
        
        Args:
            prefix: The prefix to check for.
            
        Returns:
            bool: True if any word starts with the prefix, False otherwise.
        """
        return self._get_node(prefix) is not None
    
    def get_words_with_prefix(self, prefix: str) -> list:
        """
        Get all words in the Trie that start with the given prefix.
        
        Args:
            prefix: The prefix to search for.
            
        Returns:
            list: A list of words starting with the prefix.
        """
        node = self._get_node(prefix)
        if node is None:
            return []
        
        words = []
        self._collect_words(node, prefix, words)
        return words
    
    def delete(self, word: str) -> bool:
        """
        Delete a word from the Trie.
        
        Args:
            word: The word to delete.
            
        Returns:
            bool: True if the word was deleted, False if it didn't exist.
        """
        if not self.search(word):
            return False
        
        node = self.root
        stack = []
        
        # Find the node and build a stack of nodes to potentially delete
        for char in word:
            stack.append((node, char))
            node = node.children[char]
        
        # Mark the end node as not a word
        node.is_end_of_word = False
        node.word_count -= 1
        
        # Delete nodes if they have no children and are not end of words
        while stack and not node.is_end_of_word and not node.children:
            node, char = stack.pop()
            del node.children[char]
        
        return True
    
    def _get_node(self, prefix: str) -> TrieNode:
        """
        Get the node corresponding to the last character of the prefix.
        
        Args:
            prefix: The prefix to traverse.
            
        Returns:
            TrieNode: The node at the end of the prefix, or None if not found.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def _collect_words(self, node: TrieNode, prefix: str, words: list) -> None:
        """
        Collect all words starting from the given node.
        
        Args:
            node: The current node.
            prefix: The current prefix.
            words: The list to collect words in.
        """
        if node.is_end_of_word:
            words.append(prefix)
        
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)


# Example usage
if __name__ == "__main__":
    trie = Trie()
    
    # Insert some words
    words = ["hello", "help", "hell", "helicopter", "world"]
    for word in words:
        trie.insert(word)
    
    # Search for words
    print(f"Search 'hello': {trie.search('hello')}")  # True
    print(f"Search 'help': {trie.search('help')}")    # True
    print(f"Search 'hell': {trie.search('hell')}")    # True
    print(f"Search 'helicopter': {trie.search('helicopter')}")  # True
    print(f"Search 'world': {trie.search('world')}")  # True
    print(f"Search 'helloo': {trie.search('helloo')}")  # False
    
    # Check prefixes
    print(f"Starts with 'hel': {trie.starts_with('hel')}")  # True
    print(f"Starts with 'wor': {trie.starts_with('wor')}")  # True
    print(f"Starts with 'xyz': {trie.starts_with('xyz')}")  # False
    
    # Get words with prefix
    print(f"Words with prefix 'hel': {trie.get_words_with_prefix('hel')}")
    
    # Delete a word
    print(f"Delete 'help': {trie.delete('help')}")  # True
    print(f"Search 'help' after deletion: {trie.search('help')}")  # False 
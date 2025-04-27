from collections import defaultdict, deque

class Graph:
    def __init__(self):
        """
        Initialize an empty graph
        """
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """
        Add an edge to the graph
        """
        self.graph[u].append(v)
    
    def bfs(self, start, target):
        """
        Breadth-First Search implementation
        Time Complexity: O(V + E) where V is vertices and E is edges
        Space Complexity: O(V)
        """
        # Mark all vertices as not visited
        visited = set()
        
        # Create a queue for BFS
        queue = deque([start])
        
        # Mark the start node as visited
        visited.add(start)
        
        while queue:
            # Dequeue a vertex from queue
            vertex = queue.popleft()
            
            # If this is the target, return True
            if vertex == target:
                return True
            
            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False
    
    def dfs(self, start, target):
        """
        Depth-First Search implementation
        Time Complexity: O(V + E) where V is vertices and E is edges
        Space Complexity: O(V)
        """
        # Mark all vertices as not visited
        visited = set()
        
        # Call the recursive helper function
        return self._dfs_recursive(start, target, visited)
    
    def _dfs_recursive(self, vertex, target, visited):
        """
        Helper function for recursive DFS
        """
        # Mark the current node as visited
        visited.add(vertex)
        
        # If this is the target, return True
        if vertex == target:
            return True
        
        # Recur for all adjacent vertices
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if self._dfs_recursive(neighbor, target, visited):
                    return True
        
        return False

# Example usage
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    # Test BFS
    print("BFS Search:")
    print("Path from 2 to 3 exists:", g.bfs(2, 3))
    print("Path from 3 to 0 exists:", g.bfs(3, 0))
    
    # Test DFS
    print("\nDFS Search:")
    print("Path from 2 to 3 exists:", g.dfs(2, 3))
    print("Path from 3 to 0 exists:", g.dfs(3, 0)) 
"""
Graph Implementation in Python

A graph is a data structure that consists of a set of vertices (nodes) and a set of edges
that connect these vertices. This implementation supports both directed and undirected graphs,
as well as weighted and unweighted edges.

Time Complexity:
- Add vertex: O(1)
- Add edge: O(1)
- Remove vertex: O(V + E)
- Remove edge: O(E)
- Check if edge exists: O(1)
- Get neighbors: O(1)
- BFS: O(V + E)
- DFS: O(V + E)

Space Complexity: O(V + E)
"""

from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        """
        Initialize a new graph.
        
        Args:
            directed: Whether the graph is directed (default: False)
        """
        self.graph = defaultdict(dict)
        self.directed = directed

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        
        Args:
            vertex: The vertex to add
        """
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight=1):
        """
        Add an edge to the graph.
        
        Args:
            vertex1: The first vertex
            vertex2: The second vertex
            weight: The weight of the edge (default: 1)
        """
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        self.graph[vertex1][vertex2] = weight
        if not self.directed:
            self.graph[vertex2][vertex1] = weight

    def remove_vertex(self, vertex):
        """
        Remove a vertex from the graph.
        
        Args:
            vertex: The vertex to remove
            
        Returns:
            True if the vertex was removed, False otherwise
        """
        if vertex not in self.graph:
            return False

        # Remove all edges connected to the vertex
        for v in self.graph:
            if vertex in self.graph[v]:
                del self.graph[v][vertex]

        # Remove the vertex
        del self.graph[vertex]
        return True

    def remove_edge(self, vertex1, vertex2):
        """
        Remove an edge from the graph.
        
        Args:
            vertex1: The first vertex
            vertex2: The second vertex
            
        Returns:
            True if the edge was removed, False otherwise
        """
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return False

        if vertex2 not in self.graph[vertex1]:
            return False

        del self.graph[vertex1][vertex2]
        if not self.directed:
            del self.graph[vertex2][vertex1]
        return True

    def has_edge(self, vertex1, vertex2):
        """
        Check if an edge exists between two vertices.
        
        Args:
            vertex1: The first vertex
            vertex2: The second vertex
            
        Returns:
            True if the edge exists, False otherwise
        """
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return False
        return vertex2 in self.graph[vertex1]

    def get_neighbors(self, vertex):
        """
        Get all neighbors of a vertex.
        
        Args:
            vertex: The vertex to get neighbors for
            
        Returns:
            A dictionary of neighbors and their edge weights
        """
        if vertex not in self.graph:
            return {}
        return self.graph[vertex]

    def get_vertices(self):
        """
        Get all vertices in the graph.
        
        Returns:
            A list of all vertices
        """
        return list(self.graph.keys())

    def get_edges(self):
        """
        Get all edges in the graph.
        
        Returns:
            A list of (vertex1, vertex2, weight) tuples
        """
        edges = []
        for vertex1 in self.graph:
            for vertex2, weight in self.graph[vertex1].items():
                if self.directed or vertex1 < vertex2:
                    edges.append((vertex1, vertex2, weight))
        return edges

    def bfs(self, start_vertex):
        """
        Perform a breadth-first search starting from a vertex.
        
        Args:
            start_vertex: The vertex to start the search from
            
        Returns:
            A list of vertices in BFS order
        """
        if start_vertex not in self.graph:
            return []

        visited = set()
        queue = deque([start_vertex])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

    def dfs(self, start_vertex):
        """
        Perform a depth-first search starting from a vertex.
        
        Args:
            start_vertex: The vertex to start the search from
            
        Returns:
            A list of vertices in DFS order
        """
        if start_vertex not in self.graph:
            return []

        visited = set()
        result = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)
        return result

    def is_connected(self):
        """
        Check if the graph is connected.
        
        Returns:
            True if the graph is connected, False otherwise
        """
        if not self.graph:
            return True

        start_vertex = next(iter(self.graph))
        visited = set()

        def dfs(vertex):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_vertex)
        return len(visited) == len(self.graph)

    def get_connected_components(self):
        """
        Get all connected components in the graph.
        
        Returns:
            A list of sets, where each set contains the vertices in a connected component
        """
        if not self.graph:
            return []

        visited = set()
        components = []

        def dfs(vertex, component):
            visited.add(vertex)
            component.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for vertex in self.graph:
            if vertex not in visited:
                component = set()
                dfs(vertex, component)
                components.append(component)

        return components

    def clear(self):
        """Remove all vertices and edges from the graph."""
        self.graph.clear()


# Example usage
if __name__ == "__main__":
    # Create an undirected graph
    g = Graph()
    
    # Add vertices and edges
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    g.add_edge(2, 4)
    
    print(f"Vertices: {g.get_vertices()}")  # Output: Vertices: [1, 2, 3, 4]
    print(f"Edges: {g.get_edges()}")  # Output: Edges: [(1, 2, 1), (1, 4, 1), (2, 3, 1), (2, 4, 1), (3, 4, 1)]
    
    # Check if edges exist
    print(f"Edge (1, 2) exists: {g.has_edge(1, 2)}")  # Output: Edge (1, 2) exists: True
    print(f"Edge (1, 3) exists: {g.has_edge(1, 3)}")  # Output: Edge (1, 3) exists: False
    
    # Get neighbors
    print(f"Neighbors of 2: {g.get_neighbors(2)}")  # Output: Neighbors of 2: {1: 1, 3: 1, 4: 1}
    
    # BFS and DFS
    print(f"BFS starting from 1: {g.bfs(1)}")  # Output: BFS starting from 1: [1, 2, 4, 3]
    print(f"DFS starting from 1: {g.dfs(1)}")  # Output: DFS starting from 1: [1, 2, 3, 4]
    
    # Check connectivity
    print(f"Is connected: {g.is_connected()}")  # Output: Is connected: True
    
    # Remove an edge
    g.remove_edge(2, 4)
    print(f"Edges after removing (2, 4): {g.get_edges()}")  # Output: Edges after removing (2, 4): [(1, 2, 1), (1, 4, 1), (2, 3, 1), (3, 4, 1)]
    
    # Remove a vertex
    g.remove_vertex(3)
    print(f"Vertices after removing 3: {g.get_vertices()}")  # Output: Vertices after removing 3: [1, 2, 4]
    print(f"Edges after removing 3: {g.get_edges()}")  # Output: Edges after removing 3: [(1, 2, 1), (1, 4, 1)]
    
    # Clear the graph
    g.clear()
    print(f"Vertices after clearing: {g.get_vertices()}")  # Output: Vertices after clearing: [] 
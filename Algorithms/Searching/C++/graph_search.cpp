#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

class Graph {
private:
    std::vector<std::vector<int>> adjList;
    
public:
    Graph(int vertices) {
        adjList.resize(vertices);
    }
    
    void addEdge(int u, int v) {
        adjList[u].push_back(v);
    }
    
    bool bfs(int start, int target) {
        /**
         * Breadth-First Search implementation
         * Time Complexity: O(V + E) where V is vertices and E is edges
         * Space Complexity: O(V)
         */
        std::unordered_set<int> visited;
        std::queue<int> q;
        
        // Mark the start node as visited and enqueue it
        visited.insert(start);
        q.push(start);
        
        while (!q.empty()) {
            // Dequeue a vertex from queue
            int vertex = q.front();
            q.pop();
            
            // If this is the target, return true
            if (vertex == target) {
                return true;
            }
            
            // Get all adjacent vertices of the dequeued vertex
            // If an adjacent has not been visited, then mark it
            // visited and enqueue it
            for (int neighbor : adjList[vertex]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
        
        return false;
    }
    
    bool dfs(int start, int target) {
        /**
         * Depth-First Search implementation
         * Time Complexity: O(V + E) where V is vertices and E is edges
         * Space Complexity: O(V)
         */
        std::unordered_set<int> visited;
        return dfsRecursive(start, target, visited);
    }
    
private:
    bool dfsRecursive(int vertex, int target, std::unordered_set<int>& visited) {
        // Mark the current node as visited
        visited.insert(vertex);
        
        // If this is the target, return true
        if (vertex == target) {
            return true;
        }
        
        // Recur for all adjacent vertices
        for (int neighbor : adjList[vertex]) {
            if (visited.find(neighbor) == visited.end()) {
                if (dfsRecursive(neighbor, target, visited)) {
                    return true;
                }
            }
        }
        
        return false;
    }
};

int main() {
    // Create a graph
    Graph g(4);
    
    // Add edges
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    
    // Test BFS
    std::cout << "BFS Search:" << std::endl;
    std::cout << "Path from 2 to 3 exists: " << (g.bfs(2, 3) ? "Yes" : "No") << std::endl;
    std::cout << "Path from 3 to 0 exists: " << (g.bfs(3, 0) ? "Yes" : "No") << std::endl;
    
    // Test DFS
    std::cout << "\nDFS Search:" << std::endl;
    std::cout << "Path from 2 to 3 exists: " << (g.dfs(2, 3) ? "Yes" : "No") << std::endl;
    std::cout << "Path from 3 to 0 exists: " << (g.dfs(3, 0) ? "Yes" : "No") << std::endl;
    
    return 0;
} 
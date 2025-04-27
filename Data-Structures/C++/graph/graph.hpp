/**
 * @file graph.hpp
 * @brief Graph implementation in C++
 * 
 * A graph is a data structure that consists of a set of vertices (nodes) and a set of edges
 * that connect these vertices. This implementation supports both directed and undirected graphs,
 * as well as weighted and unweighted edges.
 * 
 * Time Complexity:
 * - Add vertex: O(1)
 * - Add edge: O(1)
 * - Remove vertex: O(V + E)
 * - Remove edge: O(E)
 * - Check if edge exists: O(1)
 * - Get neighbors: O(1)
 * - BFS: O(V + E)
 * - DFS: O(V + E)
 * 
 * Space Complexity: O(V + E)
 */

#ifndef GRAPH_HPP
#define GRAPH_HPP

#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <queue>
#include <stack>
#include <stdexcept>

template<typename T>
class Graph {
private:
    std::unordered_map<T, std::unordered_map<T, int>> adjacency_list;
    bool directed;

public:
    /**
     * @brief Default constructor
     * @param directed Whether the graph is directed (default: false)
     */
    Graph(bool directed = false) : directed(directed) {}

    /**
     * @brief Add a vertex to the graph
     * @param vertex The vertex to add
     */
    void add_vertex(const T& vertex) {
        if (adjacency_list.find(vertex) == adjacency_list.end()) {
            adjacency_list[vertex] = std::unordered_map<T, int>();
        }
    }

    /**
     * @brief Add an edge to the graph
     * @param vertex1 The first vertex
     * @param vertex2 The second vertex
     * @param weight The weight of the edge (default: 1)
     */
    void add_edge(const T& vertex1, const T& vertex2, int weight = 1) {
        add_vertex(vertex1);
        add_vertex(vertex2);
        
        adjacency_list[vertex1][vertex2] = weight;
        if (!directed) {
            adjacency_list[vertex2][vertex1] = weight;
        }
    }

    /**
     * @brief Remove a vertex from the graph
     * @param vertex The vertex to remove
     * @return true if the vertex was removed, false otherwise
     */
    bool remove_vertex(const T& vertex) {
        if (adjacency_list.find(vertex) == adjacency_list.end()) {
            return false;
        }

        // Remove all edges connected to the vertex
        for (auto& [v, neighbors] : adjacency_list) {
            neighbors.erase(vertex);
        }

        // Remove the vertex
        adjacency_list.erase(vertex);
        return true;
    }

    /**
     * @brief Remove an edge from the graph
     * @param vertex1 The first vertex
     * @param vertex2 The second vertex
     * @return true if the edge was removed, false otherwise
     */
    bool remove_edge(const T& vertex1, const T& vertex2) {
        if (adjacency_list.find(vertex1) == adjacency_list.end() ||
            adjacency_list.find(vertex2) == adjacency_list.end()) {
            return false;
        }

        if (adjacency_list[vertex1].find(vertex2) == adjacency_list[vertex1].end()) {
            return false;
        }

        adjacency_list[vertex1].erase(vertex2);
        if (!directed) {
            adjacency_list[vertex2].erase(vertex1);
        }
        return true;
    }

    /**
     * @brief Check if an edge exists between two vertices
     * @param vertex1 The first vertex
     * @param vertex2 The second vertex
     * @return true if the edge exists, false otherwise
     */
    bool has_edge(const T& vertex1, const T& vertex2) const {
        if (adjacency_list.find(vertex1) == adjacency_list.end() ||
            adjacency_list.find(vertex2) == adjacency_list.end()) {
            return false;
        }
        return adjacency_list.at(vertex1).find(vertex2) != adjacency_list.at(vertex1).end();
    }

    /**
     * @brief Get all neighbors of a vertex
     * @param vertex The vertex to get neighbors for
     * @return A map of neighbors and their edge weights
     */
    std::unordered_map<T, int> get_neighbors(const T& vertex) const {
        if (adjacency_list.find(vertex) == adjacency_list.end()) {
            return {};
        }
        return adjacency_list.at(vertex);
    }

    /**
     * @brief Get all vertices in the graph
     * @return A vector of all vertices
     */
    std::vector<T> get_vertices() const {
        std::vector<T> vertices;
        for (const auto& [vertex, _] : adjacency_list) {
            vertices.push_back(vertex);
        }
        return vertices;
    }

    /**
     * @brief Get all edges in the graph
     * @return A vector of (vertex1, vertex2, weight) tuples
     */
    std::vector<std::tuple<T, T, int>> get_edges() const {
        std::vector<std::tuple<T, T, int>> edges;
        for (const auto& [vertex1, neighbors] : adjacency_list) {
            for (const auto& [vertex2, weight] : neighbors) {
                if (directed || vertex1 < vertex2) {
                    edges.emplace_back(vertex1, vertex2, weight);
                }
            }
        }
        return edges;
    }

    /**
     * @brief Perform a breadth-first search starting from a vertex
     * @param start_vertex The vertex to start the search from
     * @return A vector of vertices in BFS order
     */
    std::vector<T> bfs(const T& start_vertex) const {
        if (adjacency_list.find(start_vertex) == adjacency_list.end()) {
            return {};
        }

        std::unordered_set<T> visited;
        std::queue<T> queue;
        std::vector<T> result;

        queue.push(start_vertex);
        visited.insert(start_vertex);

        while (!queue.empty()) {
            T vertex = queue.front();
            queue.pop();
            result.push_back(vertex);

            for (const auto& [neighbor, _] : adjacency_list.at(vertex)) {
                if (visited.find(neighbor) == visited.end()) {
                    queue.push(neighbor);
                    visited.insert(neighbor);
                }
            }
        }

        return result;
    }

    /**
     * @brief Perform a depth-first search starting from a vertex
     * @param start_vertex The vertex to start the search from
     * @return A vector of vertices in DFS order
     */
    std::vector<T> dfs(const T& start_vertex) const {
        if (adjacency_list.find(start_vertex) == adjacency_list.end()) {
            return {};
        }

        std::unordered_set<T> visited;
        std::vector<T> result;

        std::function<void(const T&)> dfs_recursive = [&](const T& vertex) {
            visited.insert(vertex);
            result.push_back(vertex);

            for (const auto& [neighbor, _] : adjacency_list.at(vertex)) {
                if (visited.find(neighbor) == visited.end()) {
                    dfs_recursive(neighbor);
                }
            }
        };

        dfs_recursive(start_vertex);
        return result;
    }

    /**
     * @brief Check if the graph is connected
     * @return true if the graph is connected, false otherwise
     */
    bool is_connected() const {
        if (adjacency_list.empty()) {
            return true;
        }

        T start_vertex = adjacency_list.begin()->first;
        std::unordered_set<T> visited;

        std::function<void(const T&)> dfs = [&](const T& vertex) {
            visited.insert(vertex);
            for (const auto& [neighbor, _] : adjacency_list.at(vertex)) {
                if (visited.find(neighbor) == visited.end()) {
                    dfs(neighbor);
                }
            }
        };

        dfs(start_vertex);
        return visited.size() == adjacency_list.size();
    }

    /**
     * @brief Get all connected components in the graph
     * @return A vector of sets, where each set contains the vertices in a connected component
     */
    std::vector<std::unordered_set<T>> get_connected_components() const {
        if (adjacency_list.empty()) {
            return {};
        }

        std::unordered_set<T> visited;
        std::vector<std::unordered_set<T>> components;

        std::function<void(const T&, std::unordered_set<T>&)> dfs = [&](const T& vertex, std::unordered_set<T>& component) {
            visited.insert(vertex);
            component.insert(vertex);

            for (const auto& [neighbor, _] : adjacency_list.at(vertex)) {
                if (visited.find(neighbor) == visited.end()) {
                    dfs(neighbor, component);
                }
            }
        };

        for (const auto& [vertex, _] : adjacency_list) {
            if (visited.find(vertex) == visited.end()) {
                std::unordered_set<T> component;
                dfs(vertex, component);
                components.push_back(component);
            }
        }

        return components;
    }

    /**
     * @brief Remove all vertices and edges from the graph
     */
    void clear() {
        adjacency_list.clear();
    }
};

#endif // GRAPH_HPP 
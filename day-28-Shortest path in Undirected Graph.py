from collections import defaultdict

class Solution:
    def shortestPath(self, edges, num_nodes, num_edges, src):
        """
        Finds the shortest path in an unweighted graph from a source node to all other nodes.
        :param edges: List of tuples representing the edges in the graph (u, v)
        :param num_nodes: Total number of nodes in the graph
        :param num_edges: Total number of edges in the graph
        :param src: The source node
        :return: A list where the i-th index represents the shortest distance from the source node to node i
        """
        # Step 1: Build the adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
       
        # Step 2: Initialize variables
        visited_nodes = set([src])  # Set to keep track of visited nodes
        current_level_nodes = [src]  # List to store nodes at the current BFS level
        shortest_distances = [-1] * num_nodes  # List to store shortest distances from source to each node
        distance = 0  # Distance from the source node
       
        # Step 3: Perform BFS to calculate shortest distances
        while current_level_nodes:
            next_level_nodes = []  # List to store nodes for the next BFS level
            for node in current_level_nodes:
                shortest_distances[node] = distance  # Assign the current distance to the node
                for neighbor in graph[node]:  # Explore all neighboring nodes
                    if neighbor not in visited_nodes:  # If the neighbor has not been visited
                        next_level_nodes.append(neighbor)  # Add it to the next level nodes
                        visited_nodes.add(neighbor)  # Mark the neighbor as visited
            current_level_nodes = next_level_nodes  # Move to the next BFS level
            distance += 1  # Increment the distance
       
        return shortest_distances

## Finding shortest paths in an undirected, unweighted graph using BFS and DFS

## Matthew Sawyer 11/11/2024
## Intro to Algorithms
## Programming Assignment 2
## Python 3.10.0

import time
import re

## GLOBALS ##
adj = [[]]      # Adjacency list
V = 0           # Number of vertices in the graph

## Method to add a vertex to the graph
def add_vertex(adj, i, j): 
    if j not in adj[i]:
        adj[i].append(j)
        adj[j].append(i)

## Open the file and read the graph
def read_graph(filename): 
    global V

    with open(filename, 'r') as file: 
        for line in file: 

            # Remove all characters except numbers and commas
            line = re.sub(r'[^0-9,]', '', line)
            line = line.strip()
            
            if line:    # Ensure line is not empty

                # Split the line into two integers
                i, j = map(int, line.split(','))

                # Ensure adjacency list is large enough
                while len(adj) <= max(i, j): 
                    adj.append([])
                
                # Add the vertex to the graph
                add_vertex(adj, i, j)
                V = max(V, i + 1, j + 1)


## Method to find the shortest path using DFS
def bfs(adj, s, t): 

    if s == t:
        return 0

    global V
    visited = [False] * V
    queue = []
    distance = [0] * V

    visited[s] = True
    queue.append(s)

    while queue: 
        u = queue.pop(0)
        for v in adj[u]: 
            if not visited[v]: 
                visited[v] = True
                distance[v] = distance[u] + 1
                queue.append(v)
                if v == t: 
                    return distance[v]
    return -1       # Return -1 if no path is found
                

## Method to find the shortest path using DFS
def dfs(adj, s, t): 

    if s == t:
        return 0

    global V
    visited = [False] * V
    stack = []
    distance = [0] * V
    
    visited[s] = True
    stack.append(s)

    while stack :
        u = stack.pop()
        for v in adj[u]: 
            if not visited[v]: 
                visited[v] = True
                distance[v] = distance[u] + 1
                stack.append(v)
                if v == t: 
                    return distance[v]
    
    return -1       # Return -1 if no path is found


## Main method to run the program
if __name__ == "__main__": 

    # Read the graph from the file 
    read_graph("Test_Case_Assignment2.txt")
    
    # Print the results
    print("\n\t\t\t  BFS\t\t\t\t  DFS")
    print("Node 1\tNode 2\tDistance\tTime (ms)\tDistance\tTime (ms)")
    
    for i in range(1, V): 

        # Find time taken to run bfs
        start_time_bfs = time.time()
        shortest_path_bfs = bfs(adj, 0, i)
        end_time_bfs = time.time()
        elapsed_time_bfs = (end_time_bfs - start_time_bfs) * 1000

        # Find time taken to run dfs
        start_time_dfs = time.time()
        shortest_path_dfs = dfs(adj, 0, i)
        end_time_dfs = time.time()
        elapsed_time_dfs = (end_time_dfs - start_time_dfs) * 1000
        print(f"N_0\tN_{i} \t{shortest_path_bfs} \t\t{elapsed_time_bfs:.6f} ms\t{shortest_path_dfs} \t\t{elapsed_time_dfs:.6f} ms")

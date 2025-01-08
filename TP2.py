def create_graph_matrix(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def add_edge(matrix, start, end):
    matrix[start-1][end-1] = 1

def find_weak_components(matrix):
    size = len(matrix)
    visited = [False] * size
    count = 0
    undirected = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                undirected[i][j] = 1
                undirected[j][i] = 1
    
    def visit_connected(node):
        stack = [node]
        while stack:
            current = stack.pop()
            for next_node in range(size):
                if undirected[current][next_node] == 1 and not visited[next_node]:
                    visited[next_node] = True
                    stack.append(next_node)
    for node in range(size):
        if not visited[node]:
            count += 1
            visited[node] = True
            visit_connected(node)
    
    return count

def find_strong_components(matrix):
    size = len(matrix)
    visited = [False] * size
    count = 0
    
    def visit(node, visited_nodes):
        stack = [node]
        while stack:
            current = stack.pop()
            for next_node in range(size):
                if matrix[current][next_node] == 1 and not visited_nodes[next_node]:
                    visited_nodes[next_node] = True
                    stack.append(next_node)
    
    for node in range(size):
        if not visited[node]:
            temp_visited = [False] * size
            temp_visited[node] = True
            visit(node, temp_visited)
            reverse_visited = [False] * size
            reverse_visited[node] = True
            reversed_matrix = [[matrix[j][i] for j in range(size)] for i in range(size)]
            visit(node, reverse_visited)
            
            if not visited[node]:
                count += 1
                for i in range(size):
                    if temp_visited[i] and reverse_visited[i]:
                        visited[i] = True
    
    return count

#Test
size = 9 
matrix = create_graph_matrix(size)
edges = [
    (1, 2), (2, 3), (3, 1),  
    (4, 5), (5, 6), (6, 4),  
    (7, 8), (8, 9),          
]

for start, end in edges:
    add_edge(matrix, start, end)

print("Adjacency Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))

weak = find_weak_components(matrix)
strong = find_strong_components(matrix)

print(f"\nNumber of weakly connected components: {weak}")
print(f"Number of strongly connected components: {strong}")
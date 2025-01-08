def make_graph():
    return {}

def add_edge(graph, x, y):
    if x not in graph:
        graph[x] = []
    graph[x].append(y)

def can_reach(graph, start, end, path=None):
    if path is None:
        path = []
    
    if start == end:
        return True
        
    if start in path:
        return False
        
    path.append(start)
    
    if start in graph:
        for next_step in graph[start]:
            if can_reach(graph, next_step, end, path):
                return True
    
    return False

graph = make_graph()
edges = [
    (1, 3), (3, 5), (5, 6),
    (2, 4), (4, 6), (1, 2)
]

for x, y in edges:
    add_edge(graph, x, y)
try:
    start = int(input("Enter start node: "))
    end = int(input("Enter end node: "))
    
    # Check path
    if can_reach(graph, start, end):
        print("Path exists")
    else:
        print("No path exists")
except ValueError:
    print("Please enter valid numbers")
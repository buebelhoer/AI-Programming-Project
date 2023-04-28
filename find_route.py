import sys
import networkx as nx

def find_route(filename, start, end):
    G = nx.Graph()
    with open(filename) as infile:
        line = infile.readline()
        while line != "END OF INPUT\n":
            line = line.strip().split()
            G.add_edge(line[0],line[1],weight=int(line[2]))
            line = infile.readline()

    path =  iterativeDeepening(G, end, start)
    traceback(path)

def traceback(path):
    # No valid path found case
    if path == None:
        print("distance: infinity")
        print("route:")
        print("none")
        return
    # Start/End are the same
    if len(path) == 1:
        print("distance: 0 km")
        print("route:")
        print(f"{path[0][0]} to {path[0][0]}, 0 km")
        return
    # Normal Case
    distance = sum([x[1] for x in path])
    print(f"distance: {distance} km")
    print("route:")
    for i in range(0,len(path)-1):
        print(f"{path[i][0]} to {path[i+1][0]}, {path[i][1]} km")




def iterativeDeepening(G, end, start):
    for depth in range(G.number_of_nodes() + 1):
        path = []
        if dfs(G, start, end, path, depth):
            return path
    return None


def dfs(graph, node, goal, path, depth):
    if node == goal:
        path.append((node,0))
        return True
    if depth == 0:
        return False
    for neighbor in graph.neighbors(node):
        path.append((node,graph[node][neighbor]["weight"]))
        if dfs(graph, neighbor, goal, path, depth-1):
            return True
        path.pop()
    return False

filename = sys.argv[1]
startCity = sys.argv[2]
endCity = sys.argv[3]

find_route(filename, startCity, endCity)
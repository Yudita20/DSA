def isSafe(graph, idx, colors_array, col):
    for neighbours in graph[idx]:
        if colors_array[neighbours] == col:
            return False

    return True

def graphColoring(graph, colors_array,color, idx = 0):
    if idx == len(graph):
        return True

    for col in range(1, color+1):
        if isSafe(graph, idx, colors_array, col):
            colors_array[idx] = col
            if graphColoring(graph, colors_array, color, idx + 1):
                return True
            colors_array[col] = 0

    return False

if __name__ == "__main__":
    vertex = 4
    color = 3
    edge = 5
    edges = [(0,1),(1,2),(2,3),(3,0),(0,2)]

    graph = {i: [] for i in range(vertex)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors_array = [0] * vertex

    print(graphColoring(graph, colors_array, color))


